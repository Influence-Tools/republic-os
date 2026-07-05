---
type: Jurisdiction
title: "Houston County, AL"
classification: county
fips: "01069"
state: "AL"
demographics:
  population: 108140
  population_under_18: 24773
  population_18_64: 63161
  population_65_plus: 20206
  median_household_income: 58626
  poverty_rate: 17.51
  homeownership_rate: 63.79
  unemployment_rate: 4.5
  median_home_value: 183300
  gini_index: 0.4762
  vacancy_rate: 13.67
  race_white: 69848
  race_black: 29442
  race_asian: 1157
  race_native: 303
  hispanic: 4984
  bachelors_plus: 23639
districts:
  - to: "us/states/al/districts/01"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/al/districts/senate/29"
    rel: in-district
    area_weight: 0.874
  - to: "us/states/al/districts/senate/28"
    rel: in-district
    area_weight: 0.1256
  - to: "us/states/al/districts/house/86"
    rel: in-district
    area_weight: 0.7639
  - to: "us/states/al/districts/house/87"
    rel: in-district
    area_weight: 0.1293
  - to: "us/states/al/districts/house/85"
    rel: in-district
    area_weight: 0.0882
  - to: "us/states/al/districts/house/93"
    rel: in-district
    area_weight: 0.0182
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Houston County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 108140 |
| Under 18 | 24773 |
| 18–64 | 63161 |
| 65+ | 20206 |
| Median household income | 58626 |
| Poverty rate | 17.51 |
| Homeownership rate | 63.79 |
| Unemployment rate | 4.5 |
| Median home value | 183300 |
| Gini index | 0.4762 |
| Vacancy rate | 13.67 |
| White | 69848 |
| Black | 29442 |
| Asian | 1157 |
| Native | 303 |
| Hispanic/Latino | 4984 |
| Bachelor's or higher | 23639 |

## Districts

- [AL-01](/us/states/al/districts/01.md) — 100% (congressional)
- [AL Senate District 29](/us/states/al/districts/senate/29.md) — 87% (state senate)
- [AL Senate District 28](/us/states/al/districts/senate/28.md) — 13% (state senate)
- [AL House District 86](/us/states/al/districts/house/86.md) — 76% (state house)
- [AL House District 87](/us/states/al/districts/house/87.md) — 13% (state house)
- [AL House District 85](/us/states/al/districts/house/85.md) — 9% (state house)
- [AL House District 93](/us/states/al/districts/house/93.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
