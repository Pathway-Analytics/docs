# Tariff Configurations

> The Tariff Configuration is the set of specifications that describe the implementation of a tariff arrangement for a healthcare provider with a range of dates.

## Meta Data

### Name

Each tariff configuration will have a unique Name, this will usually indicate the year of the configuration.

### Status

The Status can be:

- `Live`: The tariff arrangement is being used for charging purposes.
- `Shadow`: The tariff arrangement is being used for testing or trial purposes.
- `Draft`: The tariff arrangement is not currently being used.

There is no difference in how we handle `Live` and `Shadow` tariffs.

### Days to Submit

Indicates the contractual obligation of the provider to make data submissions within a number of days from the prior month end.

### From / To Dates

The tariff configuration will be applied to data submitted by the participating providers organisations for months between these dates.

### Owner

The Owner is the Lead Commissioner who is responsible for communicating any changes to the tariff configuration.

## Participating Providers

The tariff configuration will be applied to participating providers who submit data for months between the configuration From / To dates.

A tariff configuration can have any number of providers associated with it.

A provider can only participate in one tariff configuration for any one particular date.

Where a healthcare provider participates in more than one tariff arrangement, then we may create separate quasi organisations to represent each arrangement they are participating in.

### Market Forces Factor

A provider may be set to have a factor applied to all the tariff rates published for the currencies in a tariff configuration. For example, a factor of 1.02 would uplift the published tariff rates by 2%. By default the Market Forces Factor is 1.000.

This allows a common tariff configuration to be shared amongst participating providers where each provider has a different factor.

This factor can include an allowance for any sort of general price adjustment such as Agenda for Change or similar allowances.

A Market Forces Factor will not be applied where a tariff configuration is using Geo-Weightings.

## Participating Commissioners

These are Local Authority Districts that either accommodate a clinic of one of the participating providers or share a common interest in the commissioning arrangement.

### Geo-Weighting

Instead of a Market Forces Factor being applied to a provider, clinics within a Local Authority District may have a Geo-Weighting applied to them. This approach allows for clinics sited in one district to have a factor that is different to clinics sited in another district.

A Geo-Weighting will not be applied where a tariff configuration is using Market Forces Factors.

## Currencies

Currencies represent a care pathway or collection of care pathways. Where a currency represents a collection of pathways, by convention they will usually be of a similar cost.

### Currency Name

The name may represent a meaningful clinical activity that collectively describes the pathways it represents, or in some cases it may be more abstract. There is a long name and a short name for each currency; in some reports and tables the short name will be used.

The name of a currency in one tariff configuration may also be used in another tariff configuration — there is no guarantee that the currencies will share any other similarities.

> :warning: A currency will only ever be charged once in any episode.

### Primary Tariff Rate

The most expensive currency in any episode will always be charged at the Primary Tariff Rate. The Primary Tariff Rate represents the full cost of the pathways delivered in the currency.

The actual rate charged will be the Primary Tariff Rate with either the provider's Market Forces Factor applied or the Commissioner's Geo-Weighting for the clinic delivering the care.

### Additional Tariff Rate

Any currency not the most expensive currency charged in an episode will be charged at the Additional Tariff Rate. The Additional Tariff Rate represents the marginal price of delivering the care represented by the currency — that is, it does not double charge for activity that is likely to be duplicated between pathways.

Occasionally, the Primary and Additional Tariff rates may be the same; this is usually where the currency is a supplement. For example, Dual Site Test is always charged as a supplement to a chlamydia and gonorrhoea test.

The actual rate charged will be the Additional Tariff Rate with either the provider's Market Forces Factor applied or the Commissioner's Geo-Weighting for the clinic delivering the care.

### Cross-Charging Arrangement

Each currency will have a cross-charging arrangement set:

- `Full Cross-Charging` (default): The commissioner of the patient's place of residence is charged. Where the patient is resident outside England and Wales the commissioner hosting the clinic delivering the care is charged.
- `Local Limited Cross-Charging`
- `Local Unlimited Cross-Charging`
- `No Cross-Charging`

### Triggers

Each currency is triggered by activity codes in the activity data submitted by the provider for that month of submission. The triggers describe the combinations of codes that may trigger a currency. Each currency can only be triggered once in each episode, no matter the number of times a trigger for the currency is matched in the episode's data.

Triggers are grouped into sets of statements. A statement must be satisfied in full by the data in one episode to raise a trigger for the currency.

Trigger statements are made up of a field name, a relational operator ('equals' or 'does not equal'), and a value with a clipped explanation, for example:

`SRH Care Activity` `=` `21 | IUD removal`

They may be strung together like this into a longer single statement:

`Contr. Main Method Status = 3 | Maintain is where the patient receives care by att...`  
`AND Contraceptive Main Method = 4 | IUS`  
`AND NOT SRH Care Activity = 20 | IUS removal`

Or like this into a collection of statements:

`Contr. Main Method Status = 3 | Maintain is where the patient receives care by att...`  
`AND Contraceptive Main Method = 4 | IUS`  
`AND NOT SRH Care Activity = 20 | IUS removal`  
***
`Contr. Main Method Status = 3 | Maintain is where the patient receives care by att...`  
`AND Contraceptive Main Method = 3 | IUD`  
`AND NOT SRH Care Activity = 21 | IUD removal`

## Invalid Currency Combinations

Some currencies are not designed to be used together or there are other reasons they should not co-occur. Invalid currency combinations allows us to address this. Each invalid combination is described by a self-explanatory statement such as:

`IF T2 Chlamydia and Gonorrhoea Test AND T7 HIV Test THEN T4 Full Screen`

## Other Terms

### Episode

An episode is a collection of activity data that shares a common Patient ID, Attendance date, Clinic ID (or equivalent) within a month of submission for a provider organisation.

> :triangular_flag_on_post: An STI test may be conducted on 28 Apr, the results may arrive back from the lab on 5 May and the patient may be seen for treatment on 8 May. All this activity will automatically be recorded as being on the 28 Apr; the diagnosis is associated with the test record and the intervention currency for the treatment is invariably triggered by the diagnosis code. So, all three activities are considered part of a single episode for tariff purposes.
>
> If the same patient was diagnosed with warts when they received their treatment for the STI test on 28 Apr, then the warts diagnosis would be entered as the 5 May and this would be the start of a new episode.

> :triangular_flag_on_post: The diagnosis is not known until after the month end, so the submission cannot be made until the test results for all the month's tests have been returned from the lab.

> :triangular_flag_on_post: The intervention currency is triggered on the diagnosis even if the patient does not attend for treatment, or if they attend at another clinic for the treatment initiated by this diagnosis — this may indeed raise a double charge for treatment.

### Local Codes

Occasionally, where the standard reporting data codes do not cover the specific activity we need to track for a tariff currency, we will provide local codes for providers to include in the activity data they submit to us.

We will usually issue the code so we can deconflict it. We will work with the commissioner to specify the precise meaning of the code and the guidance for its use.

Local codes are usually implemented within an existing reporting field such as `SHHAPT` or `Episode Activity`.

### Pathways

A pathway represents a defined sequence of clinical activities delivered to a patient within a specific clinical domain. Pathways form the basis of currency definitions.

### Currency Pathway Weighting Factor

A weighting factor applied to individual pathways within a currency to reflect relative cost differences between the pathways grouped under that currency.

### Currency Deflation Factor

A factor applied to reduce the tariff rate for a currency, typically used where economies of scale or efficiency gains are expected over time.

## Uploading Data

### Report File Formats

Providers submit activity data in defined file formats. For details on file specifications, field definitions, and validation rules, see the [Technical Guidance](/sexual-health-tariff/technical-guidance) section.
