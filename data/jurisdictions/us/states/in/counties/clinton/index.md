---
type: Jurisdiction
title: "Clinton County, IN"
classification: county
fips: "18023"
state: "IN"
demographics:
  population: 32944
  population_under_18: 8848
  population_18_64: 18759
  population_65_plus: 5337
  median_household_income: 65019
  poverty_rate: 9.85
  homeownership_rate: 74.19
  unemployment_rate: 2.61
  median_home_value: 164100
  gini_index: 0.3803
  vacancy_rate: 7.55
  race_white: 27156
  race_black: 207
  race_asian: 155
  race_native: 30
  hispanic: 6415
  bachelors_plus: 4617
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/7"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/41"
    rel: in-district
    area_weight: 0.646
  - to: "us/states/in/districts/house/38"
    rel: in-district
    area_weight: 0.354
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Clinton County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32944 |
| Under 18 | 8848 |
| 18–64 | 18759 |
| 65+ | 5337 |
| Median household income | 65019 |
| Poverty rate | 9.85 |
| Homeownership rate | 74.19 |
| Unemployment rate | 2.61 |
| Median home value | 164100 |
| Gini index | 0.3803 |
| Vacancy rate | 7.55 |
| White | 27156 |
| Black | 207 |
| Asian | 155 |
| Native | 30 |
| Hispanic/Latino | 6415 |
| Bachelor's or higher | 4617 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 7](/us/states/in/districts/senate/7.md) — 100% (state senate)
- [IN House District 41](/us/states/in/districts/house/41.md) — 65% (state house)
- [IN House District 38](/us/states/in/districts/house/38.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
