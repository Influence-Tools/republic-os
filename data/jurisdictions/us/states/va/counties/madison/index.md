---
type: Jurisdiction
title: "Madison County, VA"
classification: county
fips: "51113"
state: "VA"
demographics:
  population: 14044
  population_under_18: 2806
  population_18_64: 7979
  population_65_plus: 3259
  median_household_income: 84323
  poverty_rate: 10.76
  homeownership_rate: 77.8
  unemployment_rate: 4.33
  median_home_value: 370300
  gini_index: 0.4229
  vacancy_rate: 10.72
  race_white: 11856
  race_black: 1245
  race_asian: 53
  race_native: 2
  hispanic: 546
  bachelors_plus: 3949
districts:
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/va/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/62"
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

# Madison County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14044 |
| Under 18 | 2806 |
| 18–64 | 7979 |
| 65+ | 3259 |
| Median household income | 84323 |
| Poverty rate | 10.76 |
| Homeownership rate | 77.8 |
| Unemployment rate | 4.33 |
| Median home value | 370300 |
| Gini index | 0.4229 |
| Vacancy rate | 10.72 |
| White | 11856 |
| Black | 1245 |
| Asian | 53 |
| Native | 2 |
| Hispanic/Latino | 546 |
| Bachelor's or higher | 3949 |

## Districts

- [VA-07](/us/states/va/districts/07.md) — 100% (congressional)
- [VA Senate District 28](/us/states/va/districts/senate/28.md) — 100% (state senate)
- [VA House District 62](/us/states/va/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
