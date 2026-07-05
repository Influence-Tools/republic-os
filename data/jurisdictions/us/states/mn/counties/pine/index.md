---
type: Jurisdiction
title: "Pine County, MN"
classification: county
fips: "27115"
state: "MN"
demographics:
  population: 29640
  population_under_18: 5657
  population_18_64: 17320
  population_65_plus: 6663
  median_household_income: 71146
  poverty_rate: 11.13
  homeownership_rate: 81.61
  unemployment_rate: 5.6
  median_home_value: 239300
  gini_index: 0.4184
  vacancy_rate: 28.7
  race_white: 26217
  race_black: 704
  race_asian: 336
  race_native: 692
  hispanic: 838
  bachelors_plus: 5017
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/senate/11"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/house/11b"
    rel: in-district
    area_weight: 0.6921
  - to: "us/states/mn/districts/house/11a"
    rel: in-district
    area_weight: 0.3077
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Pine County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29640 |
| Under 18 | 5657 |
| 18–64 | 17320 |
| 65+ | 6663 |
| Median household income | 71146 |
| Poverty rate | 11.13 |
| Homeownership rate | 81.61 |
| Unemployment rate | 5.6 |
| Median home value | 239300 |
| Gini index | 0.4184 |
| Vacancy rate | 28.7 |
| White | 26217 |
| Black | 704 |
| Asian | 336 |
| Native | 692 |
| Hispanic/Latino | 838 |
| Bachelor's or higher | 5017 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 11](/us/states/mn/districts/senate/11.md) — 100% (state senate)
- [MN House District 11B](/us/states/mn/districts/house/11b.md) — 69% (state house)
- [MN House District 11A](/us/states/mn/districts/house/11a.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
