---
type: Jurisdiction
title: "Sussex County, VA"
classification: county
fips: "51183"
state: "VA"
demographics:
  population: 10765
  population_under_18: 1854
  population_18_64: 4064
  population_65_plus: 4847
  median_household_income: 63530
  poverty_rate: 11.59
  homeownership_rate: 69.75
  unemployment_rate: 4.08
  median_home_value: 183800
  gini_index: 0.4169
  vacancy_rate: 19.57
  race_white: 4382
  race_black: 5823
  race_asian: 58
  race_native: 17
  hispanic: 120
  bachelors_plus: 1848
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/senate/13"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/house/83"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Sussex County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10765 |
| Under 18 | 1854 |
| 18–64 | 4064 |
| 65+ | 4847 |
| Median household income | 63530 |
| Poverty rate | 11.59 |
| Homeownership rate | 69.75 |
| Unemployment rate | 4.08 |
| Median home value | 183800 |
| Gini index | 0.4169 |
| Vacancy rate | 19.57 |
| White | 4382 |
| Black | 5823 |
| Asian | 58 |
| Native | 17 |
| Hispanic/Latino | 120 |
| Bachelor's or higher | 1848 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 100% (congressional)
- [VA Senate District 13](/us/states/va/districts/senate/13.md) — 100% (state senate)
- [VA House District 83](/us/states/va/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
