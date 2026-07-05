---
type: Jurisdiction
title: "Johnson County, IA"
classification: county
fips: "19103"
state: "IA"
demographics:
  population: 156639
  population_under_18: 30276
  population_18_64: 105529
  population_65_plus: 20834
  median_household_income: 74935
  poverty_rate: 17.07
  homeownership_rate: 59.37
  unemployment_rate: 3.77
  median_home_value: 308600
  gini_index: 0.4985
  vacancy_rate: 7.15
  race_white: 119654
  race_black: 12059
  race_asian: 8849
  race_native: 273
  hispanic: 10554
  bachelors_plus: 74386
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ia/districts/senate/46"
    rel: in-district
    area_weight: 0.7477
  - to: "us/states/ia/districts/senate/43"
    rel: in-district
    area_weight: 0.215
  - to: "us/states/ia/districts/senate/45"
    rel: in-district
    area_weight: 0.0373
  - to: "us/states/ia/districts/house/91"
    rel: in-district
    area_weight: 0.3855
  - to: "us/states/ia/districts/house/92"
    rel: in-district
    area_weight: 0.3622
  - to: "us/states/ia/districts/house/85"
    rel: in-district
    area_weight: 0.1863
  - to: "us/states/ia/districts/house/86"
    rel: in-district
    area_weight: 0.0287
  - to: "us/states/ia/districts/house/89"
    rel: in-district
    area_weight: 0.0222
  - to: "us/states/ia/districts/house/90"
    rel: in-district
    area_weight: 0.015
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Johnson County, IA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 156639 |
| Under 18 | 30276 |
| 18–64 | 105529 |
| 65+ | 20834 |
| Median household income | 74935 |
| Poverty rate | 17.07 |
| Homeownership rate | 59.37 |
| Unemployment rate | 3.77 |
| Median home value | 308600 |
| Gini index | 0.4985 |
| Vacancy rate | 7.15 |
| White | 119654 |
| Black | 12059 |
| Asian | 8849 |
| Native | 273 |
| Hispanic/Latino | 10554 |
| Bachelor's or higher | 74386 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 46](/us/states/ia/districts/senate/46.md) — 75% (state senate)
- [IA Senate District 43](/us/states/ia/districts/senate/43.md) — 22% (state senate)
- [IA Senate District 45](/us/states/ia/districts/senate/45.md) — 4% (state senate)
- [IA House District 91](/us/states/ia/districts/house/91.md) — 39% (state house)
- [IA House District 92](/us/states/ia/districts/house/92.md) — 36% (state house)
- [IA House District 85](/us/states/ia/districts/house/85.md) — 19% (state house)
- [IA House District 86](/us/states/ia/districts/house/86.md) — 3% (state house)
- [IA House District 89](/us/states/ia/districts/house/89.md) — 2% (state house)
- [IA House District 90](/us/states/ia/districts/house/90.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
