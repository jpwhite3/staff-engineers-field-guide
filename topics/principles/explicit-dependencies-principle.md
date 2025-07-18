```markdown
# Explicit Dependencies Principle

date: "2014-11-26"
description: The Explicit Dependencies Principle states that methods and classes should explicitly require (typically through method parameters or constructor parameters) any collaborating objects they need in order to function correctly.

---

As a staff engineer, you're constantly battling systems that are overly complex, brittle, and difficult to maintain. A key contributor to these problems is often a lack of clear dependency management. The Explicit Dependencies Principle offers a straightforward solution: make your code’s needs explicit. This isn’t just about following a rule; it’s about building systems that are more resilient, testable, and ultimately, easier to evolve. Failure to adhere to this principle results in a codebase that’s a tangled mess of implicit relationships—a “new is glue” scenario where components are tightly coupled, making it difficult to understand, change, or reuse them.

## The Problem with Implicit Dependencies

When dependencies are implicit – meaning a class relies on another through mechanisms like static variables or global objects – it creates a fragile system. Imagine a large application with dozens of classes, each potentially relying on a shared static variable. Now, a small change in one class can ripple through the entire system, leading to unexpected bugs and a significant amount of rework. Testing becomes exponentially harder because you have to mock and stub *everything* that might be affected, a process known as "dependency hell.”  These implicit dependencies also introduce "god classes" – monstrously large classes that handle too much, making them the single point of failure for your application. Without explicit dependencies, you’re essentially building a house of cards—one slight disturbance, and it all collapses.

## Understanding the Principle

The Explicit Dependencies Principle states that methods and classes should explicitly require any collaborating objects they need in order to function correctly. This typically means using constructor parameters or method parameters to pass in the objects your class needs. This doesn’t mean you're creating unnecessary coupling – it’s about making the relationships clear and manageable.

Let’s break down the key concepts:

* **Collaboration:** Dependencies arise when classes work together to achieve a common goal.
* **Explicit Requirements:** Clearly defining what your class needs from other classes.
* **Constructor vs. Method Parameters:**  Class-level dependencies should be passed through the constructor. Method-level dependencies can be passed through method parameters.

## Analogy: Building a Car

Think about building a car. You wouldn’t just haphazardly throw parts together and hope it works. Instead, you’d have a blueprint that specifies exactly what components are needed—the engine, wheels, transmission, etc. Each component has a defined interface that others can interact with. Similarly, explicit dependencies define the interfaces your classes need to operate effectively.

## Real-World Examples

Here are some examples demonstrating the impact of implicit vs. explicit dependencies:

1. **Logging:**  Consider a system that needs to log events. If the logging mechanism is implemented globally (e.g., through a static logger), any class can potentially write to the log, leading to uncontrolled output and difficulty in tracing issues. Explicitly passing a logger instance to a class allows for precise control over logging behavior and enables integration with more sophisticated logging frameworks.

2. **Database Access:** Imagine a reporting class that needs to retrieve data from a database.  If the database connection is hardcoded, you've created a brittle dependency. By passing a database connection object to the class, you can easily swap out different database implementations for testing or production environments.

3. **UI Frameworks:** In complex UI frameworks (like React or Angular), components often rely on data and services provided by other components. Explicitly passing these dependencies ensures that your components are loosely coupled and can be easily reused and tested.

## The “New is Glue” Problem

This principle directly addresses the “New is Glue” problem. When new functionality is added, it’s often coupled to existing code through implicit dependencies. This means that every change can have unintended consequences, leading to a tangled, hard-to-maintain codebase. Explicit dependencies prevent this by ensuring that new functionality is built on a foundation of clearly defined interfaces.

## Code Example: Implicit Dependencies

Let’s look at a Java example demonstrating the problems with implicit dependencies.

```java lineNumbers=true
using System;
using System.IO;
using System.Linq;

namespace ImplicitDependencies
{
    class Program
    {
        static void Main(string[] args)
        {
            var customer = new Customer()
            {
                FavoriteColor = "Blue",
                Title = "Mr.",
                Fullname = "Steve Smith"
            };
            Context.CurrentCustomer = customer;

            var response = new PersonalizedResponse();

            Console.WriteLine(response.GetResponse());
            Console.ReadLine();
        }
    }

    public static class Context
    {
        public static Customer CurrentCustomer { get; set; }

        public static void Log(string message)
        {
            using (StreamWriter logFile = new StreamWriter(
                Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),
                    "logfile.txt")))
            {
                logFile.WriteLine(message);
            }
        }
    }

    public class Customer
    {
        public string FavoriteColor { get; set; }
        public string Title { get; set; }
        public string Fullname { get; set; }
    }

    public class PersonalizedResponse
    {
        public string GetResponse()
        {
            Context.Log("Generating personalized response.");
            string formatString = "Good {0}, {1} {2}! Would you like a {3} widget today?";
            string timeOfDay = "afternoon";
            if (DateTime.Now.Hour < 12)
            {
                timeOfDay = "morning";
            }
            if (DateTime.Now.Hour > 17)
            {
                timeOfDay = "evening";
            }
            return String.Format(formatString, timeOfDay,
                Context.CurrentCustomer.Title,
                Context.CurrentCustomer.Fullname,
                Context.CurrentCustomer.FavoriteColor);
        }
    }
}
```

In this example, the `PersonalizedResponse` class relies on the `Context` class for logging and the `Customer` class for data. The dependencies are not explicitly declared, making the class difficult to test, understand, and maintain.  The `Context` class has global state, making it difficult to reason about the flow of execution.

## Code Example: Explicit Dependencies

Now, let’s refactor this code to explicitly declare the dependencies.

```java lineNumbers=true
using System;
using System.IO;
using System.Linq;

namespace ExplicitDependencies
{
    class Program
    {
        static void Main(string[] args)
        {
            var customer = new Customer()
            {
                FavoriteColor = "Blue",
                Title = "Mr.",
                Fullname = "Steve Smith"
            };

            var response = new PersonalizedResponse(new SimpleFileLogger(), new SystemDateTime());

            Console.WriteLine(response.GetResponse(customer));
            Console.ReadLine();
        }
    }

    public interface ILogger
    {
        void Log(string message);
    }

    public class SimpleFileLogger : ILogger
    {
        public void Log(string message)
        {
            using (StreamWriter logFile = new StreamWriter(
                Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),
                    "logfile.txt")))
            {
                logFile.WriteLine(message);
            }
        }
    }

    public interface IDateTime
    {
        DateTime Now { get; }
    }

    public class SystemDateTime : IDateTime
    {
        public DateTime Now
        {
            get
            {
                return DateTime.Now;
            }
        }
    }

    public class Customer
    {
        public string FavoriteColor { get; set; }
        public string Title { get; set; }
        public string Fullname { get; set; }
    }

    public class PersonalizedResponse
    {
        private readonly ILogger _logger;
        private readonly IDateTime _dateTime;
        private readonly Customer _customer;

        public PersonalizedResponse(ILogger logger, IDateTime dateTime, Customer customer)
        {
            _logger = logger ?? throw new ArgumentNullException(nameof(logger));
            _dateTime = dateTime ?? throw new ArgumentNullException(nameof(dateTime));
            _customer = customer ?? throw new ArgumentNullException(nameof(customer));
        }

        public string GetResponse()
        {
            _logger.Log("Generating personalized response.");
            string formatString = "Good {0}, {1} {2}! Would you like a {3} widget today?";
            string timeOfDay = "afternoon";
            if (_dateTime.Now.Hour < 12)
            {
                timeOfDay = "morning";
            }
            if (_dateTime.Now.Hour > 17)
            {
                timeOfDay = "evening";
            }
            return String.Format(formatString, timeOfDay,
                _customer.Title,
                _customer.Fullname,
                _customer.FavoriteColor);
        }
    }
}
```

Now, the `PersonalizedResponse` class explicitly depends on an `ILogger` and `IDateTime` interface, which are implemented by concrete classes. This approach makes the class more testable, as you can easily mock these dependencies during testing. It also promotes loose coupling, allowing you to swap out different logging or time implementations without affecting the core functionality of the class.

## See Also

[Dependency Inversion Principle](/principles/dependency-inversion-principle/)

## References

[New Is Glue](http://ardalis.com/new-is-glue) (Ardalis.com)
```
