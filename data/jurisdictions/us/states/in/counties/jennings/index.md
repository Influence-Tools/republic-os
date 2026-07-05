---
type: Jurisdiction
title: "Jennings County, IN"
classification: county
fips: "18079"
state: "IN"
demographics:
  population: 27562
  population_under_18: 6377
  population_18_64: 16367
  population_65_plus: 4818
  median_household_income: 69322
  poverty_rate: 12.6
  homeownership_rate: 78.77
  unemployment_rate: 4.6
  median_home_value: 161500
  gini_index: 0.3743
  vacancy_rate: 6.71
  race_white: 25744
  race_black: 96
  race_asian: 125
  race_native: 93
  hispanic: 957
  bachelors_plus: 3792
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/senate/43"
    rel: in-district
    area_weight: 0.5378
  - to: "us/states/in/districts/senate/42"
    rel: in-district
    area_weight: 0.4621
  - to: "us/states/in/districts/house/67"
    rel: in-district
    area_weight: 0.8504
  - to: "us/states/in/districts/house/73"
    rel: in-district
    area_weight: 0.1495
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Jennings County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27562 |
| Under 18 | 6377 |
| 18–64 | 16367 |
| 65+ | 4818 |
| Median household income | 69322 |
| Poverty rate | 12.6 |
| Homeownership rate | 78.77 |
| Unemployment rate | 4.6 |
| Median home value | 161500 |
| Gini index | 0.3743 |
| Vacancy rate | 6.71 |
| White | 25744 |
| Black | 96 |
| Asian | 125 |
| Native | 93 |
| Hispanic/Latino | 957 |
| Bachelor's or higher | 3792 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 43](/us/states/in/districts/senate/43.md) — 54% (state senate)
- [IN Senate District 42](/us/states/in/districts/senate/42.md) — 46% (state senate)
- [IN House District 67](/us/states/in/districts/house/67.md) — 85% (state house)
- [IN House District 73](/us/states/in/districts/house/73.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
