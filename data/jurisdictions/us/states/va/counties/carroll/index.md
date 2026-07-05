---
type: Jurisdiction
title: "Carroll County, VA"
classification: county
fips: "51035"
state: "VA"
demographics:
  population: 29157
  population_under_18: 5126
  population_18_64: 16405
  population_65_plus: 7626
  median_household_income: 54484
  poverty_rate: 15.33
  homeownership_rate: 77.11
  unemployment_rate: 5.54
  median_home_value: 156500
  gini_index: 0.4414
  vacancy_rate: 24.68
  race_white: 27402
  race_black: 71
  race_asian: 82
  race_native: 49
  hispanic: 1191
  bachelors_plus: 4921
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/7"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/47"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Carroll County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29157 |
| Under 18 | 5126 |
| 18–64 | 16405 |
| 65+ | 7626 |
| Median household income | 54484 |
| Poverty rate | 15.33 |
| Homeownership rate | 77.11 |
| Unemployment rate | 5.54 |
| Median home value | 156500 |
| Gini index | 0.4414 |
| Vacancy rate | 24.68 |
| White | 27402 |
| Black | 71 |
| Asian | 82 |
| Native | 49 |
| Hispanic/Latino | 1191 |
| Bachelor's or higher | 4921 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 7](/us/states/va/districts/senate/7.md) — 100% (state senate)
- [VA House District 47](/us/states/va/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
