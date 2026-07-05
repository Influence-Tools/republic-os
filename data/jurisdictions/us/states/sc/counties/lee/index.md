---
type: Jurisdiction
title: "Lee County, SC"
classification: county
fips: "45061"
state: "SC"
demographics:
  population: 16166
  population_under_18: 3022
  population_18_64: 9789
  population_65_plus: 3355
  median_household_income: 44760
  poverty_rate: 24.98
  homeownership_rate: 70.49
  unemployment_rate: 6.66
  median_home_value: 104600
  gini_index: 0.4503
  vacancy_rate: 16.46
  race_white: 5512
  race_black: 10051
  race_asian: 26
  race_native: 21
  hispanic: 390
  bachelors_plus: 1841
districts:
  - to: "us/states/sc/districts/05"
    rel: in-district
    area_weight: 0.9952
  - to: "us/states/sc/districts/senate/29"
    rel: in-district
    area_weight: 0.5377
  - to: "us/states/sc/districts/senate/35"
    rel: in-district
    area_weight: 0.4622
  - to: "us/states/sc/districts/house/50"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Lee County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16166 |
| Under 18 | 3022 |
| 18–64 | 9789 |
| 65+ | 3355 |
| Median household income | 44760 |
| Poverty rate | 24.98 |
| Homeownership rate | 70.49 |
| Unemployment rate | 6.66 |
| Median home value | 104600 |
| Gini index | 0.4503 |
| Vacancy rate | 16.46 |
| White | 5512 |
| Black | 10051 |
| Asian | 26 |
| Native | 21 |
| Hispanic/Latino | 390 |
| Bachelor's or higher | 1841 |

## Districts

- [SC-05](/us/states/sc/districts/05.md) — 100% (congressional)
- [SC Senate District 29](/us/states/sc/districts/senate/29.md) — 54% (state senate)
- [SC Senate District 35](/us/states/sc/districts/senate/35.md) — 46% (state senate)
- [SC House District 50](/us/states/sc/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
