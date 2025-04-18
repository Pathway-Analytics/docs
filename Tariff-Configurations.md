# Tariff Configuration

>The Tariff Configuration is the set of specifications that describe the implementation of a tariff arrangement for a healthcare provider with a range of dates.

## Meta Data

### Name

Each tariff configuration will have a unique Name, this will usually indicate the year of the configuration.

- ### Status
  
  - `Draft`: The tariff arrangement is not currently being used.

There is no difference in how we handle `Live` and `Shadow` tariffs.

- ### Days to Submit

Indicates the contractual obligation of the provider to make data submissions within a number of days from the prior month end.

- ### From / To Dates

The tariff configuration will be applied to data submitted by the participating providers organisations for months between these dates.

- ### Owner

The Owner is the Lead Commissioner who is responsible for communicating any changes to the tariff configuration.

### Participating Providers

The tariff configuration will be applied to participating providers who submit data for months between the configuration From / To dates.

A tariff configuration can have any number of providers associated with it.  

A provider can only participate in one tariff configuration for any one particulate date.

Where a healthcare provider participates in more than one tariff arrangement, then we may create separate quasi organisations to represent each arrangement they are participating in.

- #### Market Forces Factor

A provider may be set to have a factor applied to all the tariff rates published for the currencies in a tariff configuration.  For example, a factor of 1.02 would uplift the published tariff rates by 2%.  By default the Market Forces Factor is 1.000.

This allows a common tariff configuration to be shared amongst participating providers where each provider has a different factor.

This factor can include an allowance for any sort of general price adjustment such Agenda for Change or similar allowances.

A Market Forces Factor will not be applied where a tariff configuration is using Geo-Weightings.

### Participating Commissioners

These are Local Authority Districts that either accommodate a clinic of one of the participating providers or share a common interest in the commissioning arrangement.

- #### Geo-Weighting

Instead of a Market Forces Factor being applied to a provider, clinics within a Local Authority District may have a Geo-Weighting applied to them.  This approach allows for clinics sited in one district to have a factor that is different to clinics sited in another district.

A Geo-Weighting will not be applied where a tariff configuration is using Market Forces Factors.

### Currencies

Currencies represent a care pathway or collection of care pathways.  Where a currency represents a collection of pathways, by convention they will usually be of a similar cost.

- #### Currency Name
  
  > :warning: A currency will only ever be charged once in any episode.

- #### Primary Tariff Rate

  The actual rate charged will be the Primary Tariff Rate with either the provider's Market Forces Factor applied or the Commissioner's Geo-Weighting for the clinic delivering the care.

- #### Additional Tariff Rate

  The actual rate charged will be the Additional Tariff Rate with either the provider's Market Forces Factor applied or the Commissioner's Geo-Weighting for the clinic delivering the care.

- #### Cross-Charging Arrangement

  - `No Cross-Charging`:  

- #### Triggers

Each currency is triggered by activity codes in the activity data submitted by the provider for that month of submission.  The triggers describe the combinations of codes that may trigger a currency.  Each currency can only be triggered once in each episode, no matter the number of times a trigger for the currency are matched in the episode's data.

Triggers are grouped into sets of statements, a statement must be satisfied in full by the data in one episode to raise a trigger for the currency.

Trigger statements are made up of a field name, a relational operator ('equals' or 'does not equal'), and a value with a clipped explanation, for example:

Or like this into a collection of statements:

`Contr. Main Method Status = 3 | Maintain is where the patient receives care by att...`  
`AND Contraceptive Main Method = 4 | IUS`  
`AND NOT SRH Care Activity = 20 | IUS removal`  
***
`Contr. Main Method Status = 3 | Maintain is where the patient receives care by att...`  
`AND Contraceptive Main Method = 3 | IUD`  
`AND NOT SRH Care Activity = 21 | IUD removal`

### Invalid Currency Combinations

[Edit this page on GitHub](https://github.com/Pathway-Analytics/docs/edit/main/Tariff-Configurations.md)