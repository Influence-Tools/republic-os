---
type: Jurisdiction
title: "Ottawa County, OH"
classification: county
fips: "39123"
state: "OH"
demographics:
  population: 39994
  population_under_18: 7015
  population_18_64: 21909
  population_65_plus: 11070
  median_household_income: 76101
  poverty_rate: 8.43
  homeownership_rate: 83.56
  unemployment_rate: 3.1
  median_home_value: 219900
  gini_index: 0.4646
  vacancy_rate: 36.0
  race_white: 36803
  race_black: 434
  race_asian: 168
  race_native: 66
  hispanic: 2113
  bachelors_plus: 12459
districts:
  - to: "us/states/oh/districts/09"
    rel: in-district
    area_weight: 0.4988
  - to: "us/states/oh/districts/senate/2"
    rel: in-district
    area_weight: 0.4509
  - to: "us/states/oh/districts/house/89"
    rel: in-district
    area_weight: 0.3633
  - to: "us/states/oh/districts/house/44"
    rel: in-district
    area_weight: 0.0876
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Ottawa County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39994 |
| Under 18 | 7015 |
| 18–64 | 21909 |
| 65+ | 11070 |
| Median household income | 76101 |
| Poverty rate | 8.43 |
| Homeownership rate | 83.56 |
| Unemployment rate | 3.1 |
| Median home value | 219900 |
| Gini index | 0.4646 |
| Vacancy rate | 36.0 |
| White | 36803 |
| Black | 434 |
| Asian | 168 |
| Native | 66 |
| Hispanic/Latino | 2113 |
| Bachelor's or higher | 12459 |

## Districts

- [OH-09](/us/states/oh/districts/09.md) — 50% (congressional)
- [OH Senate District 2](/us/states/oh/districts/senate/2.md) — 45% (state senate)
- [OH House District 89](/us/states/oh/districts/house/89.md) — 36% (state house)
- [OH House District 44](/us/states/oh/districts/house/44.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
