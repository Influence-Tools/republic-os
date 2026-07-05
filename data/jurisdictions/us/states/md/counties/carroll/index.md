---
type: Jurisdiction
title: "Carroll County, MD"
classification: county
fips: "24013"
state: "MD"
demographics:
  population: 175321
  population_under_18: 38635
  population_18_64: 105233
  population_65_plus: 31453
  median_household_income: 118211
  poverty_rate: 5.21
  homeownership_rate: 84.35
  unemployment_rate: 3.47
  median_home_value: 434000
  gini_index: 0.4029
  vacancy_rate: 3.72
  race_white: 150514
  race_black: 7135
  race_asian: 4207
  race_native: 382
  hispanic: 8923
  bachelors_plus: 69013
districts:
  - to: "us/states/md/districts/02"
    rel: in-district
    area_weight: 0.9013
  - to: "us/states/md/districts/03"
    rel: in-district
    area_weight: 0.0946
  - to: "us/states/md/districts/senate/5"
    rel: in-district
    area_weight: 0.7242
  - to: "us/states/md/districts/senate/42"
    rel: in-district
    area_weight: 0.2753
  - to: "us/states/md/districts/house/5"
    rel: in-district
    area_weight: 0.7242
  - to: "us/states/md/districts/house/42c"
    rel: in-district
    area_weight: 0.2753
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Carroll County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 175321 |
| Under 18 | 38635 |
| 18–64 | 105233 |
| 65+ | 31453 |
| Median household income | 118211 |
| Poverty rate | 5.21 |
| Homeownership rate | 84.35 |
| Unemployment rate | 3.47 |
| Median home value | 434000 |
| Gini index | 0.4029 |
| Vacancy rate | 3.72 |
| White | 150514 |
| Black | 7135 |
| Asian | 4207 |
| Native | 382 |
| Hispanic/Latino | 8923 |
| Bachelor's or higher | 69013 |

## Districts

- [MD-02](/us/states/md/districts/02.md) — 90% (congressional)
- [MD-03](/us/states/md/districts/03.md) — 9% (congressional)
- [MD Senate District 5](/us/states/md/districts/senate/5.md) — 72% (state senate)
- [MD Senate District 42](/us/states/md/districts/senate/42.md) — 28% (state senate)
- [MD House District 5](/us/states/md/districts/house/5.md) — 72% (state house)
- [MD House District 42C](/us/states/md/districts/house/42c.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
