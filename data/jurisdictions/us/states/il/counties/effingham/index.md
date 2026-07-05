---
type: Jurisdiction
title: "Effingham County, IL"
classification: county
fips: "17049"
state: "IL"
demographics:
  population: 34522
  population_under_18: 8265
  population_18_64: 19756
  population_65_plus: 6501
  median_household_income: 80404
  poverty_rate: 10.11
  homeownership_rate: 78.25
  unemployment_rate: 2.08
  median_home_value: 189500
  gini_index: 0.423
  vacancy_rate: 9.49
  race_white: 33062
  race_black: 101
  race_asian: 297
  race_native: 25
  hispanic: 955
  bachelors_plus: 8540
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/il/districts/senate/54"
    rel: in-district
    area_weight: 0.5892
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 0.3027
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.1082
  - to: "us/states/il/districts/house/107"
    rel: in-district
    area_weight: 0.5892
  - to: "us/states/il/districts/house/110"
    rel: in-district
    area_weight: 0.3027
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.1082
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Effingham County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34522 |
| Under 18 | 8265 |
| 18–64 | 19756 |
| 65+ | 6501 |
| Median household income | 80404 |
| Poverty rate | 10.11 |
| Homeownership rate | 78.25 |
| Unemployment rate | 2.08 |
| Median home value | 189500 |
| Gini index | 0.423 |
| Vacancy rate | 9.49 |
| White | 33062 |
| Black | 101 |
| Asian | 297 |
| Native | 25 |
| Hispanic/Latino | 955 |
| Bachelor's or higher | 8540 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 54](/us/states/il/districts/senate/54.md) — 59% (state senate)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 30% (state senate)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 11% (state senate)
- [IL House District 107](/us/states/il/districts/house/107.md) — 59% (state house)
- [IL House District 110](/us/states/il/districts/house/110.md) — 30% (state house)
- [IL House District 102](/us/states/il/districts/house/102.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
