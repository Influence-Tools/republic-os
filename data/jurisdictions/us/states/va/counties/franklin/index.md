---
type: Jurisdiction
title: "Franklin County, VA"
classification: county
fips: "51067"
state: "VA"
demographics:
  population: 55130
  population_under_18: 10201
  population_18_64: 31364
  population_65_plus: 13565
  median_household_income: 68849
  poverty_rate: 12.65
  homeownership_rate: 78.47
  unemployment_rate: 2.36
  median_home_value: 240400
  gini_index: 0.4691
  vacancy_rate: 19.04
  race_white: 47606
  race_black: 3781
  race_asian: 329
  race_native: 247
  hispanic: 2062
  bachelors_plus: 13726
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/va/districts/senate/7"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/39"
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

# Franklin County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 55130 |
| Under 18 | 10201 |
| 18–64 | 31364 |
| 65+ | 13565 |
| Median household income | 68849 |
| Poverty rate | 12.65 |
| Homeownership rate | 78.47 |
| Unemployment rate | 2.36 |
| Median home value | 240400 |
| Gini index | 0.4691 |
| Vacancy rate | 19.04 |
| White | 47606 |
| Black | 3781 |
| Asian | 329 |
| Native | 247 |
| Hispanic/Latino | 2062 |
| Bachelor's or higher | 13726 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 7](/us/states/va/districts/senate/7.md) — 100% (state senate)
- [VA House District 39](/us/states/va/districts/house/39.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
