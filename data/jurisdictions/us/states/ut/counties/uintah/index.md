---
type: Jurisdiction
title: "Uintah County, UT"
classification: county
fips: "49047"
state: "UT"
demographics:
  population: 37056
  population_under_18: 11549
  population_18_64: 21082
  population_65_plus: 4425
  median_household_income: 73746
  poverty_rate: 11.77
  homeownership_rate: 73.51
  unemployment_rate: 5.97
  median_home_value: 298600
  gini_index: 0.4365
  vacancy_rate: 12.23
  race_white: 30969
  race_black: 184
  race_asian: 316
  race_native: 1489
  hispanic: 3249
  bachelors_plus: 4703
districts:
  - to: "us/states/ut/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/house/68"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Uintah County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37056 |
| Under 18 | 11549 |
| 18–64 | 21082 |
| 65+ | 4425 |
| Median household income | 73746 |
| Poverty rate | 11.77 |
| Homeownership rate | 73.51 |
| Unemployment rate | 5.97 |
| Median home value | 298600 |
| Gini index | 0.4365 |
| Vacancy rate | 12.23 |
| White | 30969 |
| Black | 184 |
| Asian | 316 |
| Native | 1489 |
| Hispanic/Latino | 3249 |
| Bachelor's or higher | 4703 |

## Districts

- [UT-03](/us/states/ut/districts/03.md) — 100% (congressional)
- [UT Senate District 20](/us/states/ut/districts/senate/20.md) — 100% (state senate)
- [UT House District 68](/us/states/ut/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
