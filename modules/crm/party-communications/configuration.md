## Configuration 

 

Party Communications does not rely on a large standalone configuration surface. Its behavior is mainly determined by the related access model and by the integrations that create or synchronize communication records. 

 

### Source channel classification 

 

Communication records are classified by `Channel` and may be further specified by `SubChannel`. 

 

The main supported channel values are: 

 

- `Email` 

- `InstantMessage` 

- `Note`

- `SubChannel` can identify the specific origin of the communication, for example: 

 

- Outlook 

- Viber 

- WhatsApp 

 

This structure allows new integrations to be added without changing the main communication model. 

 

### Business context linking 

 

Each communication record must be linked to a `Party` and to a `DataObject`. 

 

This is not only a data requirement, but also a key part of the configuration and integration model. Without both links, communication cannot be reliably interpreted in context.
