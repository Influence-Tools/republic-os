---
type: Jurisdiction
title: "Lincoln Parish, LA"
classification: county
fips: "22061"
state: "LA"
demographics:
  population: 48174
  population_under_18: 9512
  population_18_64: 31784
  population_65_plus: 6878
  median_household_income: 39172
  poverty_rate: 31.18
  homeownership_rate: 53.76
  unemployment_rate: 3.78
  median_home_value: 210100
  gini_index: 0.5393
  vacancy_rate: 11.24
  race_white: 25631
  race_black: 17773
  race_asian: 622
  race_native: 396
  hispanic: 1778
  bachelors_plus: 13867
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/la/districts/senate/33"
    rel: in-district
    area_weight: 0.5837
  - to: "us/states/la/districts/senate/29"
    rel: in-district
    area_weight: 0.2331
  - to: "us/states/la/districts/senate/35"
    rel: in-district
    area_weight: 0.1832
  - to: "us/states/la/districts/house/12"
    rel: in-district
    area_weight: 0.7694
  - to: "us/states/la/districts/house/11"
    rel: in-district
    area_weight: 0.2306
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Lincoln Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48174 |
| Under 18 | 9512 |
| 18–64 | 31784 |
| 65+ | 6878 |
| Median household income | 39172 |
| Poverty rate | 31.18 |
| Homeownership rate | 53.76 |
| Unemployment rate | 3.78 |
| Median home value | 210100 |
| Gini index | 0.5393 |
| Vacancy rate | 11.24 |
| White | 25631 |
| Black | 17773 |
| Asian | 622 |
| Native | 396 |
| Hispanic/Latino | 1778 |
| Bachelor's or higher | 13867 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 33](/us/states/la/districts/senate/33.md) — 58% (state senate)
- [LA Senate District 29](/us/states/la/districts/senate/29.md) — 23% (state senate)
- [LA Senate District 35](/us/states/la/districts/senate/35.md) — 18% (state senate)
- [LA House District 12](/us/states/la/districts/house/12.md) — 77% (state house)
- [LA House District 11](/us/states/la/districts/house/11.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
