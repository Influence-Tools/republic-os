---
type: Jurisdiction
title: "Wood County, OH"
classification: county
fips: "39173"
state: "OH"
demographics:
  population: 132064
  population_under_18: 26719
  population_18_64: 83305
  population_65_plus: 22040
  median_household_income: 74216
  poverty_rate: 12.23
  homeownership_rate: 64.4
  unemployment_rate: 4.49
  median_home_value: 227600
  gini_index: 0.4716
  vacancy_rate: 5.88
  race_white: 115061
  race_black: 2830
  race_asian: 2805
  race_native: 236
  hispanic: 8677
  bachelors_plus: 43204
districts:
  - to: "us/states/oh/districts/05"
    rel: in-district
    area_weight: 0.8396
  - to: "us/states/oh/districts/09"
    rel: in-district
    area_weight: 0.1604
  - to: "us/states/oh/districts/senate/2"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/75"
    rel: in-district
    area_weight: 0.9548
  - to: "us/states/oh/districts/house/44"
    rel: in-district
    area_weight: 0.0452
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Wood County, OH

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 132064 |
| Under 18 | 26719 |
| 18–64 | 83305 |
| 65+ | 22040 |
| Median household income | 74216 |
| Poverty rate | 12.23 |
| Homeownership rate | 64.4 |
| Unemployment rate | 4.49 |
| Median home value | 227600 |
| Gini index | 0.4716 |
| Vacancy rate | 5.88 |
| White | 115061 |
| Black | 2830 |
| Asian | 2805 |
| Native | 236 |
| Hispanic/Latino | 8677 |
| Bachelor's or higher | 43204 |

## Districts

- [OH-05](/us/states/oh/districts/05.md) — 84% (congressional)
- [OH-09](/us/states/oh/districts/09.md) — 16% (congressional)
- [OH Senate District 2](/us/states/oh/districts/senate/2.md) — 100% (state senate)
- [OH House District 75](/us/states/oh/districts/house/75.md) — 95% (state house)
- [OH House District 44](/us/states/oh/districts/house/44.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
