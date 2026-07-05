---
type: Jurisdiction
title: "Silver Bow County, MT"
classification: county
fips: "30093"
state: "MT"
demographics:
  population: 35785
  population_under_18: 7227
  population_18_64: 21586
  population_65_plus: 6972
  median_household_income: 61754
  poverty_rate: 14.85
  homeownership_rate: 70.82
  unemployment_rate: 4.07
  median_home_value: 255200
  gini_index: 0.4702
  vacancy_rate: 11.89
  race_white: 32554
  race_black: 19
  race_asian: 141
  race_native: 700
  hispanic: 1654
  bachelors_plus: 9137
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/mt/districts/senate/35"
    rel: in-district
    area_weight: 0.5774
  - to: "us/states/mt/districts/senate/36"
    rel: in-district
    area_weight: 0.2252
  - to: "us/states/mt/districts/senate/37"
    rel: in-district
    area_weight: 0.1972
  - to: "us/states/mt/districts/house/70"
    rel: in-district
    area_weight: 0.5774
  - to: "us/states/mt/districts/house/74"
    rel: in-district
    area_weight: 0.1924
  - to: "us/states/mt/districts/house/71"
    rel: in-district
    area_weight: 0.184
  - to: "us/states/mt/districts/house/72"
    rel: in-district
    area_weight: 0.0412
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Silver Bow County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35785 |
| Under 18 | 7227 |
| 18–64 | 21586 |
| 65+ | 6972 |
| Median household income | 61754 |
| Poverty rate | 14.85 |
| Homeownership rate | 70.82 |
| Unemployment rate | 4.07 |
| Median home value | 255200 |
| Gini index | 0.4702 |
| Vacancy rate | 11.89 |
| White | 32554 |
| Black | 19 |
| Asian | 141 |
| Native | 700 |
| Hispanic/Latino | 1654 |
| Bachelor's or higher | 9137 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 35](/us/states/mt/districts/senate/35.md) — 58% (state senate)
- [MT Senate District 36](/us/states/mt/districts/senate/36.md) — 23% (state senate)
- [MT Senate District 37](/us/states/mt/districts/senate/37.md) — 20% (state senate)
- [MT House District 70](/us/states/mt/districts/house/70.md) — 58% (state house)
- [MT House District 74](/us/states/mt/districts/house/74.md) — 19% (state house)
- [MT House District 71](/us/states/mt/districts/house/71.md) — 18% (state house)
- [MT House District 72](/us/states/mt/districts/house/72.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
