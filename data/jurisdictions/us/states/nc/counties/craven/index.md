---
type: Jurisdiction
title: "Craven County, NC"
classification: county
fips: "37049"
state: "NC"
demographics:
  population: 102612
  population_under_18: 21819
  population_18_64: 59347
  population_65_plus: 21446
  median_household_income: 65873
  poverty_rate: 13.7
  homeownership_rate: 68.44
  unemployment_rate: 4.21
  median_home_value: 231600
  gini_index: 0.4495
  vacancy_rate: 11.67
  race_white: 68018
  race_black: 20249
  race_asian: 2944
  race_native: 375
  hispanic: 7996
  bachelors_plus: 26621
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.9594
  - to: "us/states/nc/districts/senate/3"
    rel: in-district
    area_weight: 0.9444
  - to: "us/states/nc/districts/house/3"
    rel: in-district
    area_weight: 0.836
  - to: "us/states/nc/districts/house/13"
    rel: in-district
    area_weight: 0.1083
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Craven County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 102612 |
| Under 18 | 21819 |
| 18–64 | 59347 |
| 65+ | 21446 |
| Median household income | 65873 |
| Poverty rate | 13.7 |
| Homeownership rate | 68.44 |
| Unemployment rate | 4.21 |
| Median home value | 231600 |
| Gini index | 0.4495 |
| Vacancy rate | 11.67 |
| White | 68018 |
| Black | 20249 |
| Asian | 2944 |
| Native | 375 |
| Hispanic/Latino | 7996 |
| Bachelor's or higher | 26621 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 96% (congressional)
- [NC Senate District 3](/us/states/nc/districts/senate/3.md) — 94% (state senate)
- [NC House District 3](/us/states/nc/districts/house/3.md) — 84% (state house)
- [NC House District 13](/us/states/nc/districts/house/13.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
