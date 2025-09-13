#!/usr/bin/env python3
"""
Targeted analysis of core field-guide pages to assess template implementation success
Focuses on the pages that were the primary targets of Issues #25, #26, #27
"""

import os
import re
from pathlib import Path
import json

# Core field-guide pages that were the focus of the template implementation phases
CORE_FIELD_GUIDE_PAGES = [
    # Archetype pages (high priority)
    "field-guide/intro/index.md",
    "field-guide/intro/tech-lead.md", 
    "field-guide/intro/architect.md",
    "field-guide/intro/solver.md",
    "field-guide/intro/right-hand.md",
    "field-guide/intro/force-multiplier.md",
    
    # Section index pages (high priority)
    "field-guide/leadership/index.md",
    "field-guide/teamwork/index.md", 
    "field-guide/execution/index.md",
    "field-guide/engineering/index.md",
    "field-guide/thinking/index.md",
    "field-guide/business/index.md",
    "field-guide/ethics/index.md",
    "field-guide/learning/index.md",
    
    # High-traffic content pages
    "field-guide/leadership/technical-vision.md",
    "field-guide/leadership/storytelling-for-engineers.md", 
    "field-guide/leadership/giving-receiving-feedback.md",
    "field-guide/teamwork/team-formation.md",
    "field-guide/teamwork/five-dysfunctions.md",
    "field-guide/teamwork/psychological-safety.md",
    "field-guide/execution/strategic-thinking.md",
    "field-guide/execution/decision-making-frameworks.md",
    "field-guide/execution/agile-essentials.md", 
    "field-guide/engineering/clean-architecture.md",
    "field-guide/engineering/site-reliability-engineering.md",
    "field-guide/engineering/continuous-delivery.md",
    "field-guide/thinking/mental-models.md",
    "field-guide/thinking/cognitive-biases.md",
    "field-guide/business/aligning-technology.md",
    "field-guide/business/product-engineering-collaboration.md",
]

def analyze_core_pages():
    """Analyze template compliance for core field-guide pages only."""
    docs_root = Path("/Users/jpwhite/Code/staff-engineers-field-guide/docs")
    
    results = {
        "core_pages_analyzed": 0,
        "fully_compliant": 0,
        "mostly_compliant": 0,
        "partially_compliant": 0,
        "not_compliant": 0,
        "has_cross_reference_navigation": 0,
        "has_further_reading": 0,
        "has_assessment_integration": 0,
        "total_broken_links": 0,
        "page_details": []
    }
    
    for page_path in CORE_FIELD_GUIDE_PAGES:
        full_path = docs_root / page_path
        if not full_path.exists():
            print(f"⚠️  Missing: {page_path}")
            continue
            
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Analyze this page
        page_analysis = {
            "path": page_path,
            "word_count": len(content.split()),
            "has_cross_reference_navigation": bool(re.search(r'## Cross-Reference Navigation', content, re.IGNORECASE)),
            "has_further_reading": bool(re.search(r'## Further Reading', content, re.IGNORECASE)),
            "has_assessment_integration": bool(re.search(r'\[.*Assessment.*\]\(.*appendix/tools.*\)', content, re.IGNORECASE)),
            "broken_links": []
        }
        
        # Calculate compliance score
        score = 0
        if page_analysis["word_count"] > 1000:
            score += 10
        if page_analysis["has_cross_reference_navigation"]:
            score += 30
        if page_analysis["has_further_reading"]:
            score += 25
        if page_analysis["has_assessment_integration"]:
            score += 20
        
        # Check for broken links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.findall(link_pattern, content)
        
        for link_text, link_url in links:
            if not link_url.startswith(('http', 'mailto:', '#')):
                # It's a relative link, check if it exists
                try:
                    current_dir = full_path.parent
                    clean_url = link_url.split('#')[0]
                    if clean_url:
                        resolved = (current_dir / clean_url).resolve()
                        try:
                            resolved.relative_to(docs_root)
                            if not resolved.exists():
                                page_analysis["broken_links"].append(link_url)
                        except ValueError:
                            pass
                except Exception:
                    pass
        
        # Check citation format
        citation_issues = []
        further_reading_match = re.search(r'## Further Reading(.*?)(?=\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
        if further_reading_match:
            further_reading_content = further_reading_match.group(1)
            citation_pattern = r'^[-*]\s+(.+?)\.?\s*\*([^*]+)\*\.?\s*(\d{4})\.?(.*)$'
            lines = further_reading_content.strip().split('\n')
            
            for line in lines:
                line = line.strip()
                if line.startswith(('- ', '* ')) and '*' in line:
                    if not re.match(citation_pattern, line):
                        citation_issues.append(line[:50])
        
        if not citation_issues:
            score += 15
            
        page_analysis["compliance_score"] = score
        page_analysis["citation_issues"] = len(citation_issues)
        
        # Categorize compliance
        if score >= 85:
            page_analysis["status"] = "FULLY_COMPLIANT"
            results["fully_compliant"] += 1
        elif score >= 60:
            page_analysis["status"] = "MOSTLY_COMPLIANT"  
            results["mostly_compliant"] += 1
        elif score >= 30:
            page_analysis["status"] = "PARTIALLY_COMPLIANT"
            results["partially_compliant"] += 1
        else:
            page_analysis["status"] = "NOT_COMPLIANT"
            results["not_compliant"] += 1
        
        # Update aggregates
        results["core_pages_analyzed"] += 1
        if page_analysis["has_cross_reference_navigation"]:
            results["has_cross_reference_navigation"] += 1
        if page_analysis["has_further_reading"]:
            results["has_further_reading"] += 1
        if page_analysis["has_assessment_integration"]:
            results["has_assessment_integration"] += 1
        results["total_broken_links"] += len(page_analysis["broken_links"])
        
        results["page_details"].append(page_analysis)
    
    return results

def main():
    print("🎯 CORE FIELD-GUIDE PAGES TEMPLATE COMPLIANCE ANALYSIS")
    print("="*70)
    print(f"Analyzing {len(CORE_FIELD_GUIDE_PAGES)} core field-guide pages that were the focus of Issues #25-27")
    print()
    
    results = analyze_core_pages()
    
    # Calculate percentages
    total = results["core_pages_analyzed"]
    if total == 0:
        print("❌ No core pages found to analyze!")
        return
        
    compliance_rate = (results["fully_compliant"] + results["mostly_compliant"]) / total * 100
    cross_ref_rate = results["has_cross_reference_navigation"] / total * 100
    further_reading_rate = results["has_further_reading"] / total * 100
    assessment_rate = results["has_assessment_integration"] / total * 100
    broken_link_rate = results["total_broken_links"] / max(1, sum(len(p["broken_links"]) for p in results["page_details"])) * 100 if results["total_broken_links"] > 0 else 0
    
    print(f"📊 CORE PAGES SUMMARY:")
    print(f"  Total Core Pages: {total}")
    print(f"  Template Compliance Rate: {compliance_rate:.1f}%")
    print(f"  Cross-Reference Navigation: {results['has_cross_reference_navigation']}/{total} ({cross_ref_rate:.1f}%)")
    print(f"  Further Reading Sections: {results['has_further_reading']}/{total} ({further_reading_rate:.1f}%)")
    print(f"  Assessment Integration: {results['has_assessment_integration']}/{total} ({assessment_rate:.1f}%)")
    print(f"  Total Broken Links: {results['total_broken_links']}")
    print()
    
    print(f"🎯 TARGET ACHIEVEMENT (Core Pages Only):")
    print(f"  Template Compliance: {'✅' if compliance_rate >= 85 else '❌'} {compliance_rate:.1f}% (Target: 85%)")
    print(f"  Cross-Reference Coverage: {'✅' if cross_ref_rate >= 80 else '❌'} {cross_ref_rate:.1f}% (Target: 80%+)")
    print(f"  Further Reading Coverage: {'✅' if further_reading_rate >= 70 else '❌'} {further_reading_rate:.1f}% (Target: 70%+)")
    print()
    
    print(f"📈 COMPLIANCE BREAKDOWN:")
    print(f"  FULLY_COMPLIANT: {results['fully_compliant']} pages")
    print(f"  MOSTLY_COMPLIANT: {results['mostly_compliant']} pages")
    print(f"  PARTIALLY_COMPLIANT: {results['partially_compliant']} pages")
    print(f"  NOT_COMPLIANT: {results['not_compliant']} pages")
    print()
    
    # Show pages that need attention
    needs_work = [p for p in results["page_details"] if p["status"] in ["NOT_COMPLIANT", "PARTIALLY_COMPLIANT"]]
    if needs_work:
        print(f"🔍 CORE PAGES NEEDING ATTENTION ({len(needs_work)} pages):")
        for page in needs_work:
            print(f"  • {page['path']} - {page['status']} ({page['compliance_score']}/100)")
            if page['broken_links']:
                print(f"    Broken links: {', '.join(page['broken_links'][:3])}{'...' if len(page['broken_links']) > 3 else ''}")
    else:
        print("🎉 All core pages meet minimum compliance standards!")
    
    print()
    print(f"💡 RECOMMENDATIONS:")
    
    if cross_ref_rate < 80:
        missing_cross_ref = [p for p in results["page_details"] if not p["has_cross_reference_navigation"]]
        print(f"  • Add Cross-Reference Navigation to {len(missing_cross_ref)} pages")
    
    if further_reading_rate < 70:
        missing_further_reading = [p for p in results["page_details"] if not p["has_further_reading"]]
        print(f"  • Add Further Reading sections to {len(missing_further_reading)} pages")
        
    if results["total_broken_links"] > 0:
        print(f"  • Fix {results['total_broken_links']} broken links across core pages")
    
    if compliance_rate >= 85:
        print("  🎉 Core field-guide pages are successfully template-compliant!")
        print("  🎯 Focus next on extending compliance to remaining content pages")
    
    return results

if __name__ == "__main__":
    main()