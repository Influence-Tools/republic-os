---
type: Jurisdiction
title: "Greene County, OH"
classification: county
fips: "39057"
state: "OH"
demographics:
  population: 169688
  population_under_18: 34890
  population_18_64: 103247
  population_65_plus: 31551
  median_household_income: 87309
  poverty_rate: 9.84
  homeownership_rate: 67.99
  unemployment_rate: 4.3
  median_home_value: 252200
  gini_index: 0.4273
  vacancy_rate: 5.84
  race_white: 139223
  race_black: 10118
  race_asian: 5095
  race_native: 246
  hispanic: 5613
  bachelors_plus: 71369
districts:
  - to: "us/states/oh/districts/10"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/oh/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/71"
    rel: in-district
    area_weight: 0.6341
  - to: "us/states/oh/districts/house/70"
    rel: in-district
    area_weight: 0.3658
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Greene County, OH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 169688 |
| Under 18 | 34890 |
| 18–64 | 103247 |
| 65+ | 31551 |
| Median household income | 87309 |
| Poverty rate | 9.84 |
| Homeownership rate | 67.99 |
| Unemployment rate | 4.3 |
| Median home value | 252200 |
| Gini index | 0.4273 |
| Vacancy rate | 5.84 |
| White | 139223 |
| Black | 10118 |
| Asian | 5095 |
| Native | 246 |
| Hispanic/Latino | 5613 |
| Bachelor's or higher | 71369 |

## Districts

- [OH-10](/us/states/oh/districts/10.md) — 100% (congressional)
- [OH Senate District 10](/us/states/oh/districts/senate/10.md) — 100% (state senate)
- [OH House District 71](/us/states/oh/districts/house/71.md) — 63% (state house)
- [OH House District 70](/us/states/oh/districts/house/70.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
