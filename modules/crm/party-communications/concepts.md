## Concepts 

 

### Unified communication model 

 

Party Communications uses a single model for multiple communication types. 

 

Instead of keeping separate storage and review logic for each channel, the system stores different communication records in one common structure. This makes it possible to build a consolidated timeline, apply consistent filtering, and keep a uniform audit trail. 

 

The communication type is determined by `Channel`, while `SubChannel` provides more specific source information when needed. 

 

### Direction and participants 

 

The communication direction is stored in `Direction` and indicates whether the record is inbound or outbound. 

 

The primary participants are represented by: 

 

- `CommunicationFrom` 

- `CommunicationTo` 

 

This provides a normalized way to store the main sender and recipient regardless of the original channel. 

 

For email and chat scenarios, this supports a consistent view across different communication sources. 

 

### External synchronization and de-duplication 

 

A major design goal of Party Communications is to support integrations without losing control over identity and traceability. 

 

When communication is synchronized from external systems, the system can store: 

 

- the source system name in `ExternalSystem` 

- the source record identifier in `ExternalId` 

 

This allows synchronization logic to recognize existing records and avoid creating duplicates during repeated imports or updates. 

 

### Notes versus discussions 

 

Internal notes in Party Communications are not the same as discussion messages. 

 

Discussion features are intended for internal collaboration and conversation flow. Party Communications notes are intended to remain part of a structured and traceable communication history linked to a party and a business object. 

 

This distinction is important because Party Communications focuses on a normalized communication log with consistent metadata, filtering, and timeline behavior. 

 

### Communication as an aggregate timeline 

 

Party Communications should be understood as an aggregate communication layer. 

 

It is not limited to one channel and it is not tied to one specific user interface pattern. Its role is to provide a common place where communication events from different origins can be stored, identified, linked, and later visualized as: 

 

- a timeline 

- a channel-based list 

- a context-specific communication history 

 

This model makes future integrations easier to extend and helps preserve continuity across communication channels. 
