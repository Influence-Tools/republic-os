---
type: Jurisdiction
title: "Campbell County, VA"
classification: county
fips: "51031"
state: "VA"
demographics:
  population: 55312
  population_under_18: 10718
  population_18_64: 32823
  population_65_plus: 11771
  median_household_income: 66165
  poverty_rate: 10.81
  homeownership_rate: 74.95
  unemployment_rate: 3.71
  median_home_value: 211600
  gini_index: 0.4152
  vacancy_rate: 12.9
  race_white: 42771
  race_black: 7860
  race_asian: 576
  race_native: 18
  hispanic: 1924
  bachelors_plus: 13892
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/8"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/51"
    rel: in-district
    area_weight: 0.9899
  - to: "us/states/va/districts/house/52"
    rel: in-district
    area_weight: 0.0099
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Campbell County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 55312 |
| Under 18 | 10718 |
| 18–64 | 32823 |
| 65+ | 11771 |
| Median household income | 66165 |
| Poverty rate | 10.81 |
| Homeownership rate | 74.95 |
| Unemployment rate | 3.71 |
| Median home value | 211600 |
| Gini index | 0.4152 |
| Vacancy rate | 12.9 |
| White | 42771 |
| Black | 7860 |
| Asian | 576 |
| Native | 18 |
| Hispanic/Latino | 1924 |
| Bachelor's or higher | 13892 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 8](/us/states/va/districts/senate/8.md) — 100% (state senate)
- [VA House District 51](/us/states/va/districts/house/51.md) — 99% (state house)
- [VA House District 52](/us/states/va/districts/house/52.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
