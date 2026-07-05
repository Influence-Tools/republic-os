---
type: Jurisdiction
title: "Hamilton County, IA"
classification: county
fips: "19079"
state: "IA"
demographics:
  population: 14886
  population_under_18: 3547
  population_18_64: 8182
  population_65_plus: 3157
  median_household_income: 72432
  poverty_rate: 7.4
  homeownership_rate: 73.38
  unemployment_rate: 4.85
  median_home_value: 156400
  gini_index: 0.4378
  vacancy_rate: 8.61
  race_white: 12870
  race_black: 144
  race_asian: 338
  race_native: 49
  hispanic: 1510
  bachelors_plus: 3043
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/55"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Hamilton County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14886 |
| Under 18 | 3547 |
| 18–64 | 8182 |
| 65+ | 3157 |
| Median household income | 72432 |
| Poverty rate | 7.4 |
| Homeownership rate | 73.38 |
| Unemployment rate | 4.85 |
| Median home value | 156400 |
| Gini index | 0.4378 |
| Vacancy rate | 8.61 |
| White | 12870 |
| Black | 144 |
| Asian | 338 |
| Native | 49 |
| Hispanic/Latino | 1510 |
| Bachelor's or higher | 3043 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 28](/us/states/ia/districts/senate/28.md) — 100% (state senate)
- [IA House District 55](/us/states/ia/districts/house/55.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
