---
type: Jurisdiction
title: "Grayson County, VA"
classification: county
fips: "51077"
state: "VA"
demographics:
  population: 15287
  population_under_18: 2480
  population_18_64: 8832
  population_65_plus: 3975
  median_household_income: 47730
  poverty_rate: 16.47
  homeownership_rate: 80.43
  unemployment_rate: 3.59
  median_home_value: 150100
  gini_index: 0.5014
  vacancy_rate: 29.28
  race_white: 13405
  race_black: 841
  race_asian: 157
  race_native: 0
  hispanic: 641
  bachelors_plus: 2398
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/va/districts/senate/7"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/house/46"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Grayson County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15287 |
| Under 18 | 2480 |
| 18–64 | 8832 |
| 65+ | 3975 |
| Median household income | 47730 |
| Poverty rate | 16.47 |
| Homeownership rate | 80.43 |
| Unemployment rate | 3.59 |
| Median home value | 150100 |
| Gini index | 0.5014 |
| Vacancy rate | 29.28 |
| White | 13405 |
| Black | 841 |
| Asian | 157 |
| Native | 0 |
| Hispanic/Latino | 641 |
| Bachelor's or higher | 2398 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 7](/us/states/va/districts/senate/7.md) — 100% (state senate)
- [VA House District 46](/us/states/va/districts/house/46.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
