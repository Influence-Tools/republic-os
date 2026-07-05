---
type: Jurisdiction
title: "Benton County, MS"
classification: county
fips: "28009"
state: "MS"
demographics:
  population: 7589
  population_under_18: 1598
  population_18_64: 4398
  population_65_plus: 1593
  median_household_income: 46016
  poverty_rate: 21.52
  homeownership_rate: 85.98
  unemployment_rate: 3.13
  median_home_value: 105100
  gini_index: 0.4444
  vacancy_rate: 24.86
  race_white: 4613
  race_black: 2616
  race_asian: 25
  race_native: 7
  hispanic: 183
  bachelors_plus: 961
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/house/13"
    rel: in-district
    area_weight: 0.7932
  - to: "us/states/ms/districts/house/5"
    rel: in-district
    area_weight: 0.2065
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Benton County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7589 |
| Under 18 | 1598 |
| 18–64 | 4398 |
| 65+ | 1593 |
| Median household income | 46016 |
| Poverty rate | 21.52 |
| Homeownership rate | 85.98 |
| Unemployment rate | 3.13 |
| Median home value | 105100 |
| Gini index | 0.4444 |
| Vacancy rate | 24.86 |
| White | 4613 |
| Black | 2616 |
| Asian | 25 |
| Native | 7 |
| Hispanic/Latino | 183 |
| Bachelor's or higher | 961 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 3](/us/states/ms/districts/senate/3.md) — 100% (state senate)
- [MS House District 13](/us/states/ms/districts/house/13.md) — 79% (state house)
- [MS House District 5](/us/states/ms/districts/house/5.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
