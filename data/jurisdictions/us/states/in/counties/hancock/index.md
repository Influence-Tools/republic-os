---
type: Jurisdiction
title: "Hancock County, IN"
classification: county
fips: "18059"
state: "IN"
demographics:
  population: 84037
  population_under_18: 19505
  population_18_64: 49991
  population_65_plus: 14541
  median_household_income: 93186
  poverty_rate: 4.74
  homeownership_rate: 79.52
  unemployment_rate: 2.73
  median_home_value: 274800
  gini_index: 0.4051
  vacancy_rate: 2.61
  race_white: 74567
  race_black: 2960
  race_asian: 945
  race_native: 73
  hispanic: 2952
  bachelors_plus: 27147
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/senate/28"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/53"
    rel: in-district
    area_weight: 0.6663
  - to: "us/states/in/districts/house/88"
    rel: in-district
    area_weight: 0.2364
  - to: "us/states/in/districts/house/54"
    rel: in-district
    area_weight: 0.0971
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Hancock County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 84037 |
| Under 18 | 19505 |
| 18–64 | 49991 |
| 65+ | 14541 |
| Median household income | 93186 |
| Poverty rate | 4.74 |
| Homeownership rate | 79.52 |
| Unemployment rate | 2.73 |
| Median home value | 274800 |
| Gini index | 0.4051 |
| Vacancy rate | 2.61 |
| White | 74567 |
| Black | 2960 |
| Asian | 945 |
| Native | 73 |
| Hispanic/Latino | 2952 |
| Bachelor's or higher | 27147 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 100% (congressional)
- [IN Senate District 28](/us/states/in/districts/senate/28.md) — 100% (state senate)
- [IN House District 53](/us/states/in/districts/house/53.md) — 67% (state house)
- [IN House District 88](/us/states/in/districts/house/88.md) — 24% (state house)
- [IN House District 54](/us/states/in/districts/house/54.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
