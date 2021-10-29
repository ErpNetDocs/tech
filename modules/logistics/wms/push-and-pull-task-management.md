# Push and pull task management

When a warehouse requisition document comes in, there are many ways we can plan how to fulfil it. The plan is represented by warehouse order documents.
 
But how are these order documents created? There are at least two main ways to organize the work.
 
## Pull system

The pull system is the easiest way to organize the execution. Under some circumstances, it can also be the most efficient.
 
In the pull system, each warehouse worker decides when to get (pull) work. Whenever they are ready, they request more work through their mobile app.
 
Pros:
 
- Do not require a central planner.
- Effective for small orders, usually e-commerce.
- Very easy to set up.
- Easy to maintain - no need to plan for workers missing, overloaded, etc.
- Efficient - workers achieve high efficiency without central planning (but might need more control).

Cons:
 
- Not good for B2B, because large orders are better served with push system.
- Without a central planner, worker control needs to be better controlled.
- Cannot implement complex order mixing, splitting or other complex work procedures.
 
## Push system

Under the push system, there is a central planner, who plans the work and pushes it to the workers. The push system might be required in more complicated execution environments.
 
Pros:
 
- A central planner can better allocate the worker and machine resources to fulfil the requisitions.
- In complicated execution, the pull system might be inappropriate.
- Worker task management is taken away from the workers and controlled centrally.

Cons:
 
- More expensive - require a central planner.
- The efficiency of the workers depends heavily on the planner. 
 
## Choosing The right strategy

There can be other organizations of the workflow within a warehouse. The @@name data model allows implementing almost any conceivable strategy, with the most prominent ones built-in.
 
However, planning the execution can be externalized to custom apps and services. Applying AI/ML strategies for achieving better efficiency is a possible direction.
 
Also, mixing robots with human workers might require using custom strategies.

