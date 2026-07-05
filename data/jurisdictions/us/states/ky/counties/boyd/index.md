---
type: Jurisdiction
title: "Boyd County, KY"
classification: county
fips: "21019"
state: "KY"
demographics:
  population: 47911
  population_under_18: 10159
  population_18_64: 27927
  population_65_plus: 9825
  median_household_income: 61118
  poverty_rate: 16.95
  homeownership_rate: 70.17
  unemployment_rate: 6.4
  median_home_value: 130700
  gini_index: 0.4582
  vacancy_rate: 11.19
  race_white: 44517
  race_black: 1124
  race_asian: 172
  race_native: 47
  hispanic: 873
  bachelors_plus: 9948
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/ky/districts/senate/18"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/house/100"
    rel: in-district
    area_weight: 0.5616
  - to: "us/states/ky/districts/house/96"
    rel: in-district
    area_weight: 0.3573
  - to: "us/states/ky/districts/house/98"
    rel: in-district
    area_weight: 0.0807
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Boyd County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47911 |
| Under 18 | 10159 |
| 18–64 | 27927 |
| 65+ | 9825 |
| Median household income | 61118 |
| Poverty rate | 16.95 |
| Homeownership rate | 70.17 |
| Unemployment rate | 6.4 |
| Median home value | 130700 |
| Gini index | 0.4582 |
| Vacancy rate | 11.19 |
| White | 44517 |
| Black | 1124 |
| Asian | 172 |
| Native | 47 |
| Hispanic/Latino | 873 |
| Bachelor's or higher | 9948 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 18](/us/states/ky/districts/senate/18.md) — 100% (state senate)
- [KY House District 100](/us/states/ky/districts/house/100.md) — 56% (state house)
- [KY House District 96](/us/states/ky/districts/house/96.md) — 36% (state house)
- [KY House District 98](/us/states/ky/districts/house/98.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
