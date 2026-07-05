---
type: Jurisdiction
title: "Highland County, VA"
classification: county
fips: "51091"
state: "VA"
demographics:
  population: 2296
  population_under_18: 334
  population_18_64: 1164
  population_65_plus: 798
  median_household_income: 65625
  poverty_rate: 9.54
  homeownership_rate: 88.93
  unemployment_rate: 11.95
  median_home_value: 200000
  gini_index: 0.3707
  vacancy_rate: 46.19
  race_white: 2179
  race_black: 0
  race_asian: 55
  race_native: 0
  hispanic: 0
  bachelors_plus: 718
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/va/districts/senate/2"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/house/35"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Highland County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2296 |
| Under 18 | 334 |
| 18–64 | 1164 |
| 65+ | 798 |
| Median household income | 65625 |
| Poverty rate | 9.54 |
| Homeownership rate | 88.93 |
| Unemployment rate | 11.95 |
| Median home value | 200000 |
| Gini index | 0.3707 |
| Vacancy rate | 46.19 |
| White | 2179 |
| Black | 0 |
| Asian | 55 |
| Native | 0 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 718 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 2](/us/states/va/districts/senate/2.md) — 100% (state senate)
- [VA House District 35](/us/states/va/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
