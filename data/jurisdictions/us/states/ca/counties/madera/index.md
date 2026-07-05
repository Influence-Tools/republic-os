---
type: Jurisdiction
title: "Madera County, CA"
classification: county
fips: "06039"
state: "CA"
demographics:
  population: 160940
  population_under_18: 43672
  population_18_64: 94120
  population_65_plus: 23148
  median_household_income: 76627
  poverty_rate: 19.2
  homeownership_rate: 67.46
  unemployment_rate: 10.12
  median_home_value: 393200
  gini_index: 0.4591
  vacancy_rate: 11.05
  race_white: 60715
  race_black: 4158
  race_asian: 3846
  race_native: 3326
  hispanic: 98083
  bachelors_plus: 24432
districts:
  - to: "us/states/ca/districts/05"
    rel: in-district
    area_weight: 0.686
  - to: "us/states/ca/districts/13"
    rel: in-district
    area_weight: 0.313
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.7378
  - to: "us/states/ca/districts/senate/14"
    rel: in-district
    area_weight: 0.2621
  - to: "us/states/ca/districts/house/8"
    rel: in-district
    area_weight: 0.7751
  - to: "us/states/ca/districts/house/27"
    rel: in-district
    area_weight: 0.2249
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Madera County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 160940 |
| Under 18 | 43672 |
| 18–64 | 94120 |
| 65+ | 23148 |
| Median household income | 76627 |
| Poverty rate | 19.2 |
| Homeownership rate | 67.46 |
| Unemployment rate | 10.12 |
| Median home value | 393200 |
| Gini index | 0.4591 |
| Vacancy rate | 11.05 |
| White | 60715 |
| Black | 4158 |
| Asian | 3846 |
| Native | 3326 |
| Hispanic/Latino | 98083 |
| Bachelor's or higher | 24432 |

## Districts

- [CA-05](/us/states/ca/districts/05.md) — 69% (congressional)
- [CA-13](/us/states/ca/districts/13.md) — 31% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 74% (state senate)
- [CA Senate District 14](/us/states/ca/districts/senate/14.md) — 26% (state senate)
- [CA House District 8](/us/states/ca/districts/house/8.md) — 78% (state house)
- [CA House District 27](/us/states/ca/districts/house/27.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
