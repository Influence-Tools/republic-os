---
type: Jurisdiction
title: "Gibson County, IN"
classification: county
fips: "18051"
state: "IN"
demographics:
  population: 33000
  population_under_18: 7810
  population_18_64: 19183
  population_65_plus: 6007
  median_household_income: 67573
  poverty_rate: 10.79
  homeownership_rate: 76.7
  unemployment_rate: 2.33
  median_home_value: 180000
  gini_index: 0.4115
  vacancy_rate: 9.75
  race_white: 29840
  race_black: 606
  race_asian: 189
  race_native: 11
  hispanic: 767
  bachelors_plus: 5383
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/in/districts/senate/48"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/in/districts/house/64"
    rel: in-district
    area_weight: 0.8384
  - to: "us/states/in/districts/house/75"
    rel: in-district
    area_weight: 0.1611
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Gibson County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33000 |
| Under 18 | 7810 |
| 18–64 | 19183 |
| 65+ | 6007 |
| Median household income | 67573 |
| Poverty rate | 10.79 |
| Homeownership rate | 76.7 |
| Unemployment rate | 2.33 |
| Median home value | 180000 |
| Gini index | 0.4115 |
| Vacancy rate | 9.75 |
| White | 29840 |
| Black | 606 |
| Asian | 189 |
| Native | 11 |
| Hispanic/Latino | 767 |
| Bachelor's or higher | 5383 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 48](/us/states/in/districts/senate/48.md) — 100% (state senate)
- [IN House District 64](/us/states/in/districts/house/64.md) — 84% (state house)
- [IN House District 75](/us/states/in/districts/house/75.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
