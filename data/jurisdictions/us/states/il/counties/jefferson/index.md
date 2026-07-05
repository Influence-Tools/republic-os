---
type: Jurisdiction
title: "Jefferson County, IL"
classification: county
fips: "17081"
state: "IL"
demographics:
  population: 36550
  population_under_18: 8140
  population_18_64: 21112
  population_65_plus: 7298
  median_household_income: 63118
  poverty_rate: 13.53
  homeownership_rate: 71.68
  unemployment_rate: 5.78
  median_home_value: 126000
  gini_index: 0.4335
  vacancy_rate: 10.88
  race_white: 30687
  race_black: 2272
  race_asian: 376
  race_native: 122
  hispanic: 1030
  bachelors_plus: 6420
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/116"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Jefferson County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36550 |
| Under 18 | 8140 |
| 18–64 | 21112 |
| 65+ | 7298 |
| Median household income | 63118 |
| Poverty rate | 13.53 |
| Homeownership rate | 71.68 |
| Unemployment rate | 5.78 |
| Median home value | 126000 |
| Gini index | 0.4335 |
| Vacancy rate | 10.88 |
| White | 30687 |
| Black | 2272 |
| Asian | 376 |
| Native | 122 |
| Hispanic/Latino | 1030 |
| Bachelor's or higher | 6420 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 100% (state senate)
- [IL House District 116](/us/states/il/districts/house/116.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
