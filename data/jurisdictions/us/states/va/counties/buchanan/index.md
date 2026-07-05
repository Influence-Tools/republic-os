---
type: Jurisdiction
title: "Buchanan County, VA"
classification: county
fips: "51027"
state: "VA"
demographics:
  population: 19415
  population_under_18: 3252
  population_18_64: 11530
  population_65_plus: 4633
  median_household_income: 42886
  poverty_rate: 25.22
  homeownership_rate: 83.07
  unemployment_rate: 3.86
  median_home_value: 94900
  gini_index: 0.4653
  vacancy_rate: 27.04
  race_white: 18205
  race_black: 751
  race_asian: 152
  race_native: 8
  hispanic: 213
  bachelors_plus: 2522
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/va/districts/house/43"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Buchanan County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19415 |
| Under 18 | 3252 |
| 18–64 | 11530 |
| 65+ | 4633 |
| Median household income | 42886 |
| Poverty rate | 25.22 |
| Homeownership rate | 83.07 |
| Unemployment rate | 3.86 |
| Median home value | 94900 |
| Gini index | 0.4653 |
| Vacancy rate | 27.04 |
| White | 18205 |
| Black | 751 |
| Asian | 152 |
| Native | 8 |
| Hispanic/Latino | 213 |
| Bachelor's or higher | 2522 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 43](/us/states/va/districts/house/43.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
