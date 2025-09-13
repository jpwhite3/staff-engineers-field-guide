#!/usr/bin/env python3
"""
Quality Assurance Validation Script for Staff Engineer's Field Guide Template Implementation
Validates template compliance across all modified pages from Issues #25, #26, #27
"""

import os
import re
from pathlib import Path
import json
from typing import Dict, List, Tuple, Any
from collections import defaultdict

class FieldGuideQAValidator:
    def __init__(self, docs_root: str):
        self.docs_root = Path(docs_root)
        self.validation_results = defaultdict(dict)
        self.cross_references = []
        self.broken_links = []
        
    def validate_page(self, file_path: Path) -> Dict[str, Any]:
        """Validate a single page against template standards."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {"error": f"Could not read file: {e}", "status": "ERROR"}
            
        result = {
            "file_path": str(file_path.relative_to(self.docs_root)),
            "word_count": len(content.split()),
            "has_cross_reference_navigation": False,
            "has_further_reading": False,
            "has_assessment_integration": False,
            "cross_references": [],
            "broken_links": [],
            "citation_format_issues": [],
            "template_compliance_score": 0,
            "compliance_status": "NOT_COMPLIANT"
        }
        
        # Check for Cross-Reference Navigation section
        cross_ref_pattern = r'## Cross-Reference Navigation'
        if re.search(cross_ref_pattern, content, re.IGNORECASE):
            result["has_cross_reference_navigation"] = True
            result["template_compliance_score"] += 30
            
        # Check for Further Reading section
        further_reading_pattern = r'## Further Reading'
        if re.search(further_reading_pattern, content, re.IGNORECASE):
            result["has_further_reading"] = True
            result["template_compliance_score"] += 25
            
        # Check for Assessment Tool integration
        assessment_pattern = r'\[.*Assessment.*\]\(.*appendix/tools.*\)'
        if re.search(assessment_pattern, content, re.IGNORECASE):
            result["has_assessment_integration"] = True
            result["template_compliance_score"] += 20
            
        # Extract all cross-references (markdown links)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.findall(link_pattern, content)
        
        for link_text, link_url in links:
            if not link_url.startswith(('http', 'mailto:', '#')):
                # It's a relative link, check if it exists
                full_link_path = self._resolve_relative_path(file_path, link_url)
                result["cross_references"].append({
                    "text": link_text,
                    "url": link_url,
                    "resolved_path": str(full_link_path) if full_link_path else None,
                    "exists": full_link_path and full_link_path.exists() if full_link_path else False
                })
                
                if full_link_path and not full_link_path.exists():
                    result["broken_links"].append(link_url)
                    
        # Check citation format in Further Reading
        citation_issues = self._check_citation_format(content)
        result["citation_format_issues"] = citation_issues
        if not citation_issues:
            result["template_compliance_score"] += 15
            
        # Additional points for content depth (substantial pages)
        if result["word_count"] > 1000:
            result["template_compliance_score"] += 10
            
        # Determine compliance status
        if result["template_compliance_score"] >= 85:
            result["compliance_status"] = "FULLY_COMPLIANT"
        elif result["template_compliance_score"] >= 60:
            result["compliance_status"] = "MOSTLY_COMPLIANT"
        elif result["template_compliance_score"] >= 30:
            result["compliance_status"] = "PARTIALLY_COMPLIANT"
        else:
            result["compliance_status"] = "NOT_COMPLIANT"
            
        return result
        
    def _resolve_relative_path(self, current_file: Path, relative_url: str) -> Path:
        """Resolve relative path from current file location."""
        try:
            # Remove anchor fragments
            clean_url = relative_url.split('#')[0]
            if not clean_url:
                return None
                
            # Resolve relative to current file's directory
            current_dir = current_file.parent
            resolved = (current_dir / clean_url).resolve()
            
            # Make sure it's still within the docs directory
            try:
                resolved.relative_to(self.docs_root)
                return resolved
            except ValueError:
                return None
        except Exception:
            return None
            
    def _check_citation_format(self, content: str) -> List[str]:
        """Check for proper citation format in Further Reading sections."""
        issues = []
        
        # Extract Further Reading section
        further_reading_match = re.search(
            r'## Further Reading(.*?)(?=\n##|\Z)', 
            content, 
            re.DOTALL | re.IGNORECASE
        )
        
        if further_reading_match:
            further_reading_content = further_reading_match.group(1)
            
            # Look for citation patterns - should be Author, Title. Year format
            citation_pattern = r'^[-*]\s+(.+?)\.?\s*\*([^*]+)\*\.?\s*(\d{4})\.?(.*)$'
            lines = further_reading_content.strip().split('\n')
            
            for i, line in enumerate(lines, 1):
                line = line.strip()
                if line.startswith(('- ', '* ')) and '*' in line:
                    if not re.match(citation_pattern, line):
                        issues.append(f"Line {i}: Improper citation format - '{line[:50]}...'")
                        
        return issues
        
    def validate_all_pages(self, target_files: List[str] = None) -> Dict[str, Any]:
        """Validate all pages or specific target files."""
        
        if target_files:
            pages_to_validate = [self.docs_root / f for f in target_files if (self.docs_root / f).exists()]
        else:
            pages_to_validate = list(self.docs_root.rglob("*.md"))
            
        total_pages = len(pages_to_validate)
        compliant_pages = 0
        total_cross_references = 0
        total_broken_links = 0
        
        print(f"Validating {total_pages} pages...")
        
        for page_path in pages_to_validate:
            if page_path.name == "index.md" and str(page_path).endswith("/docs/index.md"):
                continue  # Skip main index
                
            result = self.validate_page(page_path)
            self.validation_results[str(page_path.relative_to(self.docs_root))] = result
            
            # Aggregate statistics
            total_cross_references += len(result["cross_references"])
            total_broken_links += len(result["broken_links"])
            
            if result["compliance_status"] in ["FULLY_COMPLIANT", "MOSTLY_COMPLIANT"]:
                compliant_pages += 1
                
            # Progress indicator
            print(f"  ✓ {page_path.name} - {result['compliance_status']} ({result['template_compliance_score']}/100)")
            
        # Generate summary report
        compliance_rate = (compliant_pages / total_pages * 100) if total_pages > 0 else 0
        
        summary = {
            "total_pages_validated": total_pages,
            "compliant_pages": compliant_pages,
            "compliance_rate_percent": compliance_rate,
            "total_cross_references": total_cross_references,
            "total_broken_links": total_broken_links,
            "broken_link_rate_percent": (total_broken_links / total_cross_references * 100) if total_cross_references > 0 else 0,
            "validation_timestamp": "2025-09-12"
        }
        
        return {
            "summary": summary,
            "detailed_results": dict(self.validation_results),
            "target_metrics": {
                "template_compliance_target": "85%",
                "cross_reference_target": "300+",
                "broken_link_target": "<2%"
            }
        }
        
    def generate_report(self, output_file: str = None):
        """Generate comprehensive validation report."""
        if not self.validation_results:
            print("No validation results available. Run validate_all_pages() first.")
            return
            
        validation_data = self.validate_all_pages()
        
        # Console report
        print("\n" + "="*80)
        print("STAFF ENGINEER'S FIELD GUIDE - TEMPLATE IMPLEMENTATION QA REPORT")
        print("="*80)
        
        summary = validation_data["summary"]
        print(f"\n📊 SUMMARY METRICS:")
        print(f"  Total Pages Validated: {summary['total_pages_validated']}")
        print(f"  Template Compliance Rate: {summary['compliance_rate_percent']:.1f}%")
        print(f"  Total Cross References: {summary['total_cross_references']}")
        print(f"  Broken Links: {summary['total_broken_links']}")
        print(f"  Broken Link Rate: {summary['broken_link_rate_percent']:.1f}%")
        
        # Target achievement
        print(f"\n🎯 TARGET ACHIEVEMENT:")
        print(f"  Template Compliance: {'✅' if summary['compliance_rate_percent'] >= 85 else '❌'} {summary['compliance_rate_percent']:.1f}% (Target: 85%)")
        print(f"  Cross References: {'✅' if summary['total_cross_references'] >= 300 else '❌'} {summary['total_cross_references']} (Target: 300+)")
        print(f"  Broken Link Rate: {'✅' if summary['broken_link_rate_percent'] < 2 else '❌'} {summary['broken_link_rate_percent']:.1f}% (Target: <2%)")
        
        # Compliance breakdown
        compliance_breakdown = defaultdict(int)
        for result in validation_data["detailed_results"].values():
            compliance_breakdown[result["compliance_status"]] += 1
            
        print(f"\n📈 COMPLIANCE BREAKDOWN:")
        for status, count in compliance_breakdown.items():
            print(f"  {status}: {count} pages")
            
        # Most common issues
        print(f"\n🔍 ISSUES REQUIRING ATTENTION:")
        needs_attention = [
            (path, result) for path, result in validation_data["detailed_results"].items()
            if result["compliance_status"] in ["NOT_COMPLIANT", "PARTIALLY_COMPLIANT"]
        ]
        
        if needs_attention:
            print(f"  {len(needs_attention)} pages need template compliance improvements:")
            for path, result in needs_attention[:10]:  # Show first 10
                print(f"    • {path} - {result['compliance_status']} ({result['template_compliance_score']}/100)")
        else:
            print("  🎉 All pages meet minimum compliance standards!")
            
        # Save detailed report if requested
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(validation_data, f, indent=2, ensure_ascii=False)
            print(f"\n💾 Detailed report saved to: {output_file}")
            
        return validation_data


def main():
    """Main execution function."""
    docs_root = "/Users/jpwhite/Code/staff-engineers-field-guide/docs"
    
    # Define the target files from Issues #25, #26, #27 (67 total pages)
    # This would ideally be populated from the actual issue descriptions
    target_files = [
        # Core field guide pages
        "field-guide/intro/index.md",
        "field-guide/intro/tech-lead.md",
        "field-guide/intro/architect.md", 
        "field-guide/intro/solver.md",
        "field-guide/intro/right-hand.md",
        "field-guide/leadership/index.md",
        "field-guide/teamwork/index.md",
        "field-guide/execution/index.md",
        "field-guide/engineering/index.md",
        "field-guide/thinking/index.md",
        "field-guide/business/index.md",
        "field-guide/ethics/index.md",
        "field-guide/learning/index.md",
        # Add more specific pages as identified from the issues
    ]
    
    validator = FieldGuideQAValidator(docs_root)
    
    print("🔍 Starting Template Implementation Quality Assurance Validation...")
    print(f"📁 Validating documents in: {docs_root}")
    
    # Run validation on all markdown files (since we don't have exact lists from issues)
    report_data = validator.validate_all_pages()
    
    # Generate comprehensive report
    validator.generate_report("template-qa-report.json")
    
    print(f"\n✅ Quality assurance validation completed!")
    print("📋 Review the detailed results above and address any compliance issues identified.")

if __name__ == "__main__":
    main()