---
type: Jurisdiction
title: "Washington County, VA"
classification: county
fips: "51191"
state: "VA"
demographics:
  population: 53926
  population_under_18: 10710
  population_18_64: 14823
  population_65_plus: 28393
  median_household_income: 64552
  poverty_rate: 11.07
  homeownership_rate: 75.78
  unemployment_rate: 2.97
  median_home_value: 214000
  gini_index: 0.4914
  vacancy_rate: 13.52
  race_white: 50961
  race_black: 981
  race_asian: 272
  race_native: 42
  hispanic: 1001
  bachelors_plus: 14680
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/44"
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

# Washington County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53926 |
| Under 18 | 10710 |
| 18–64 | 14823 |
| 65+ | 28393 |
| Median household income | 64552 |
| Poverty rate | 11.07 |
| Homeownership rate | 75.78 |
| Unemployment rate | 2.97 |
| Median home value | 214000 |
| Gini index | 0.4914 |
| Vacancy rate | 13.52 |
| White | 50961 |
| Black | 981 |
| Asian | 272 |
| Native | 42 |
| Hispanic/Latino | 1001 |
| Bachelor's or higher | 14680 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 44](/us/states/va/districts/house/44.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
