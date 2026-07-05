---
type: Jurisdiction
title: "Albany County, NY"
classification: county
fips: "36001"
state: "NY"
demographics:
  population: 317018
  population_under_18: 57145
  population_18_64: 202271
  population_65_plus: 57602
  median_household_income: 85333
  poverty_rate: 13.03
  homeownership_rate: 56.58
  unemployment_rate: 5.04
  median_home_value: 294600
  gini_index: 0.4557
  vacancy_rate: 8.78
  race_white: 219405
  race_black: 39144
  race_asian: 24574
  race_native: 357
  hispanic: 22986
  bachelors_plus: 148336
districts:
  - to: "us/states/ny/districts/20"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ny/districts/senate/46"
    rel: in-district
    area_weight: 0.8788
  - to: "us/states/ny/districts/senate/43"
    rel: in-district
    area_weight: 0.1211
  - to: "us/states/ny/districts/house/102"
    rel: in-district
    area_weight: 0.5542
  - to: "us/states/ny/districts/house/109"
    rel: in-district
    area_weight: 0.2333
  - to: "us/states/ny/districts/house/110"
    rel: in-district
    area_weight: 0.1357
  - to: "us/states/ny/districts/house/107"
    rel: in-district
    area_weight: 0.0643
  - to: "us/states/ny/districts/house/108"
    rel: in-district
    area_weight: 0.0125
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Albany County, NY

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 317018 |
| Under 18 | 57145 |
| 18–64 | 202271 |
| 65+ | 57602 |
| Median household income | 85333 |
| Poverty rate | 13.03 |
| Homeownership rate | 56.58 |
| Unemployment rate | 5.04 |
| Median home value | 294600 |
| Gini index | 0.4557 |
| Vacancy rate | 8.78 |
| White | 219405 |
| Black | 39144 |
| Asian | 24574 |
| Native | 357 |
| Hispanic/Latino | 22986 |
| Bachelor's or higher | 148336 |

## Districts

- [NY-20](/us/states/ny/districts/20.md) — 100% (congressional)
- [NY Senate District 46](/us/states/ny/districts/senate/46.md) — 88% (state senate)
- [NY Senate District 43](/us/states/ny/districts/senate/43.md) — 12% (state senate)
- [NY House District 102](/us/states/ny/districts/house/102.md) — 55% (state house)
- [NY House District 109](/us/states/ny/districts/house/109.md) — 23% (state house)
- [NY House District 110](/us/states/ny/districts/house/110.md) — 14% (state house)
- [NY House District 107](/us/states/ny/districts/house/107.md) — 6% (state house)
- [NY House District 108](/us/states/ny/districts/house/108.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
