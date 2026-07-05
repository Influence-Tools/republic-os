---
type: Jurisdiction
title: "Dallas County, IA"
classification: county
fips: "19049"
state: "IA"
demographics:
  population: 107968
  population_under_18: 28676
  population_18_64: 65399
  population_65_plus: 13893
  median_household_income: 102379
  poverty_rate: 6.26
  homeownership_rate: 69.05
  unemployment_rate: 2.29
  median_home_value: 355600
  gini_index: 0.44
  vacancy_rate: 5.21
  race_white: 90607
  race_black: 3189
  race_asian: 5263
  race_native: 186
  hispanic: 7453
  bachelors_plus: 49277
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/24"
    rel: in-district
    area_weight: 0.3747
  - to: "us/states/ia/districts/senate/23"
    rel: in-district
    area_weight: 0.2217
  - to: "us/states/ia/districts/senate/14"
    rel: in-district
    area_weight: 0.204
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 0.1977
  - to: "us/states/ia/districts/house/47"
    rel: in-district
    area_weight: 0.3746
  - to: "us/states/ia/districts/house/46"
    rel: in-district
    area_weight: 0.2217
  - to: "us/states/ia/districts/house/23"
    rel: in-district
    area_weight: 0.1977
  - to: "us/states/ia/districts/house/28"
    rel: in-district
    area_weight: 0.1598
  - to: "us/states/ia/districts/house/27"
    rel: in-district
    area_weight: 0.0442
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Dallas County, IA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 107968 |
| Under 18 | 28676 |
| 18–64 | 65399 |
| 65+ | 13893 |
| Median household income | 102379 |
| Poverty rate | 6.26 |
| Homeownership rate | 69.05 |
| Unemployment rate | 2.29 |
| Median home value | 355600 |
| Gini index | 0.44 |
| Vacancy rate | 5.21 |
| White | 90607 |
| Black | 3189 |
| Asian | 5263 |
| Native | 186 |
| Hispanic/Latino | 7453 |
| Bachelor's or higher | 49277 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 24](/us/states/ia/districts/senate/24.md) — 37% (state senate)
- [IA Senate District 23](/us/states/ia/districts/senate/23.md) — 22% (state senate)
- [IA Senate District 14](/us/states/ia/districts/senate/14.md) — 20% (state senate)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 20% (state senate)
- [IA House District 47](/us/states/ia/districts/house/47.md) — 37% (state house)
- [IA House District 46](/us/states/ia/districts/house/46.md) — 22% (state house)
- [IA House District 23](/us/states/ia/districts/house/23.md) — 20% (state house)
- [IA House District 28](/us/states/ia/districts/house/28.md) — 16% (state house)
- [IA House District 27](/us/states/ia/districts/house/27.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
