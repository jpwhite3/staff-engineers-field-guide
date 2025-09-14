---
title: Domain-Driven Design (DDD)
description: Align software architecture with business domain complexity through strategic design patterns and tactical modeling techniques.
tags:
  - domain-driven-design
  - architecture
  - modeling
  - bounded-context
  - ubiquitous-language
  - strategic-design
  - tactical-design
---

# Domain-Driven Design (DDD)

!!! quote "Domain Excellence"
    *"The heart of software is its ability to solve domain-related problems for its user."*

    **— Eric Evans, Domain-Driven Design**

Domain-Driven Design provides a framework for tackling complex software projects by focusing the design on the core business domain and domain logic. For staff engineers, DDD offers strategic and tactical patterns for building software that truly serves business needs while remaining maintainable and extensible.

## Strategic Design Patterns

### Bounded Context

Define clear boundaries around domain models to manage complexity:

**Characteristics:**
- Clear ownership of domain concepts
- Consistent language within boundaries
- Explicit interfaces between contexts
- Independent evolution of models

**Implementation:**
- Map organizational boundaries to technical boundaries
- Define context boundaries early in design
- Maintain boundary integrity through interfaces
- Document context relationships and dependencies

### Ubiquitous Language

Establish shared vocabulary between domain experts and developers:

**Development Process:**
- Collaborate closely with domain experts
- Use domain terminology in code and documentation
- Evolve language as understanding deepens
- Ensure consistency across team communication

### Context Mapping

Understand relationships between different bounded contexts:

**Relationship Patterns:**
- **Partnership**: Teams coordinate closely on interface evolution
- **Customer/Supplier**: Downstream team depends on upstream team
- **Conformist**: Downstream team accepts upstream team's model
- **Anti-Corruption Layer**: Protect local model from external influences

## Tactical Design Patterns

### Entities

Model objects that have identity and lifecycle:

```python
class Order:
    def __init__(self, order_id: OrderId, customer: Customer):
        self._id = order_id
        self._customer = customer
        self._items = []
        self._status = OrderStatus.DRAFT

    @property
    def id(self) -> OrderId:
        return self._id

    def add_item(self, item: OrderItem) -> None:
        if self._status != OrderStatus.DRAFT:
            raise DomainException("Cannot modify confirmed order")
        self._items.append(item)
```

### Value Objects

Model immutable concepts that are defined by their attributes:

```python
@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: Currency

    def add(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise DomainException("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)
```

### Aggregates

Design consistency boundaries for groups of related entities:

**Aggregate Rules:**
- One entity serves as the aggregate root
- External objects reference only the root
- Internal objects cannot be directly accessed
- Aggregate maintains invariants

### Domain Services

Implement domain logic that doesn't belong to entities or value objects:

```python
class PricingService:
    def __init__(self, pricing_repository: PricingRepository):
        self._pricing_repo = pricing_repository

    def calculate_order_total(self, order: Order) -> Money:
        base_total = sum(item.total for item in order.items)
        discount = self._calculate_discount(order)
        return base_total.subtract(discount)
```

### Repositories

Provide collection-like interface for accessing aggregates:

```python
class OrderRepository(ABC):
    @abstractmethod
    def find_by_id(self, order_id: OrderId) -> Optional[Order]:
        pass

    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def find_by_customer(self, customer_id: CustomerId) -> List[Order]:
        pass
```

### Domain Events

Capture important business events for decoupled communication:

```python
@dataclass
class OrderConfirmedEvent:
    order_id: OrderId
    customer_id: CustomerId
    total_amount: Money
    confirmed_at: datetime

class Order:
    def confirm(self) -> None:
        if self._status != OrderStatus.DRAFT:
            raise DomainException("Order already confirmed")

        self._status = OrderStatus.CONFIRMED
        self._confirmed_at = datetime.utcnow()

        # Raise domain event
        self._events.append(OrderConfirmedEvent(
            self._id, self._customer.id, self.total, self._confirmed_at
        ))
```

## Implementation Patterns

### Hexagonal Architecture Integration

Align DDD with hexagonal architecture principles:

**Application Layer**: Orchestrates domain operations and handles use cases
**Domain Layer**: Contains business logic, entities, and domain services
**Infrastructure Layer**: Implements repositories and external integrations
**Presentation Layer**: Handles user interface and API concerns

### Event Sourcing with DDD

Store domain events as the source of truth:

**Benefits:**
- Complete audit trail of domain changes
- Ability to rebuild state from events
- Support for temporal queries
- Integration with event-driven architectures

**Implementation Considerations:**
- Design events to capture business intent
- Handle event versioning and schema evolution
- Implement efficient event storage and retrieval
- Consider snapshot strategies for performance

### CQRS Integration

Separate command and query responsibilities:

**Command Side**: Optimized for writing and domain operations
**Query Side**: Optimized for reading and reporting
**Event Integration**: Use domain events to synchronize sides

## Cross-Reference Navigation

**Architecture Integration:**
- **[Clean Architecture](../../field-guide/engineering/clean-architecture.md)** - Architectural patterns that complement DDD
- **[Hexagonal Architecture](../../field-guide/engineering/hexagonal-architecture.md)** - Port and adapter pattern alignment with DDD
- **[Technical Architecture](../../field-guide/engineering/technical-architecture.md)** - System design considerations for DDD

**Design Patterns:**
- **[State Design Pattern](state-design-pattern.md)** - Behavioral pattern useful in domain modeling
- **[Strategy Pattern](strategy-pattern.md)** - Encapsulating business rules and algorithms

**Business Integration:**
- **[Product Engineering Collaboration](../../field-guide/business/product-engineering-collaboration.md)** - Working with domain experts
- **[Strategic Thinking](../../field-guide/execution/strategic-thinking.md)** - Strategic approaches to domain modeling

## Further Reading

This appendix draws on domain-driven design experts and practitioners:

*   **Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software*.** The foundational text that established DDD principles and practices.
*   **Vernon, Vaughn. *Implementing Domain-Driven Design*.** Practical guide to implementing DDD in real-world projects.
*   **Millett, Scott, and Nick Tune. *Patterns, Principles, and Practices of Domain-Driven Design*.** Comprehensive guide to both strategic and tactical DDD patterns.
*   **Khononov, Vlad. *Learning Domain-Driven Design: Aligning Software Architecture and Business Strategy*.** Modern approach to DDD with practical examples and case studies.