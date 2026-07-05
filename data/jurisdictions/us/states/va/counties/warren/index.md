---
type: Jurisdiction
title: "Warren County, VA"
classification: county
fips: "51187"
state: "VA"
demographics:
  population: 41531
  population_under_18: 9757
  population_18_64: 13300
  population_65_plus: 18474
  median_household_income: 84682
  poverty_rate: 11.64
  homeownership_rate: 75.85
  unemployment_rate: 4.88
  median_home_value: 348400
  gini_index: 0.4173
  vacancy_rate: 10.11
  race_white: 34270
  race_black: 2160
  race_asian: 561
  race_native: 46
  hispanic: 3064
  bachelors_plus: 10155
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9962
  - to: "us/states/va/districts/senate/1"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/house/31"
    rel: in-district
    area_weight: 0.7268
  - to: "us/states/va/districts/house/33"
    rel: in-district
    area_weight: 0.2729
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Warren County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41531 |
| Under 18 | 9757 |
| 18–64 | 13300 |
| 65+ | 18474 |
| Median household income | 84682 |
| Poverty rate | 11.64 |
| Homeownership rate | 75.85 |
| Unemployment rate | 4.88 |
| Median home value | 348400 |
| Gini index | 0.4173 |
| Vacancy rate | 10.11 |
| White | 34270 |
| Black | 2160 |
| Asian | 561 |
| Native | 46 |
| Hispanic/Latino | 3064 |
| Bachelor's or higher | 10155 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 1](/us/states/va/districts/senate/1.md) — 100% (state senate)
- [VA House District 31](/us/states/va/districts/house/31.md) — 73% (state house)
- [VA House District 33](/us/states/va/districts/house/33.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
