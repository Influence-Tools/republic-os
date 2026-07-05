---
type: Jurisdiction
title: "Washington County, IL"
classification: county
fips: "17189"
state: "IL"
demographics:
  population: 13627
  population_under_18: 2836
  population_18_64: 7843
  population_65_plus: 2948
  median_household_income: 78224
  poverty_rate: 7.53
  homeownership_rate: 84.11
  unemployment_rate: 4.35
  median_home_value: 155700
  gini_index: 0.4025
  vacancy_rate: 9.66
  race_white: 12968
  race_black: 202
  race_asian: 32
  race_native: 20
  hispanic: 217
  bachelors_plus: 3117
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 0.676
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.324
  - to: "us/states/il/districts/house/109"
    rel: in-district
    area_weight: 0.6758
  - to: "us/states/il/districts/house/115"
    rel: in-district
    area_weight: 0.3036
  - to: "us/states/il/districts/house/116"
    rel: in-district
    area_weight: 0.0204
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Washington County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13627 |
| Under 18 | 2836 |
| 18–64 | 7843 |
| 65+ | 2948 |
| Median household income | 78224 |
| Poverty rate | 7.53 |
| Homeownership rate | 84.11 |
| Unemployment rate | 4.35 |
| Median home value | 155700 |
| Gini index | 0.4025 |
| Vacancy rate | 9.66 |
| White | 12968 |
| Black | 202 |
| Asian | 32 |
| Native | 20 |
| Hispanic/Latino | 217 |
| Bachelor's or higher | 3117 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 68% (state senate)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 32% (state senate)
- [IL House District 109](/us/states/il/districts/house/109.md) — 68% (state house)
- [IL House District 115](/us/states/il/districts/house/115.md) — 30% (state house)
- [IL House District 116](/us/states/il/districts/house/116.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
