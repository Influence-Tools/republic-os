---
type: Jurisdiction
title: "Mississippi County, AR"
classification: county
fips: "05093"
state: "AR"
demographics:
  population: 39126
  population_under_18: 10126
  population_18_64: 22915
  population_65_plus: 6085
  median_household_income: 52548
  poverty_rate: 21.13
  homeownership_rate: 59.95
  unemployment_rate: 6.9
  median_home_value: 122500
  gini_index: 0.5122
  vacancy_rate: 19.24
  race_white: 22227
  race_black: 13466
  race_asian: 203
  race_native: 72
  hispanic: 1911
  bachelors_plus: 4920
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ar/districts/senate/19"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ar/districts/house/33"
    rel: in-district
    area_weight: 0.5334
  - to: "us/states/ar/districts/house/34"
    rel: in-district
    area_weight: 0.4659
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Mississippi County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39126 |
| Under 18 | 10126 |
| 18–64 | 22915 |
| 65+ | 6085 |
| Median household income | 52548 |
| Poverty rate | 21.13 |
| Homeownership rate | 59.95 |
| Unemployment rate | 6.9 |
| Median home value | 122500 |
| Gini index | 0.5122 |
| Vacancy rate | 19.24 |
| White | 22227 |
| Black | 13466 |
| Asian | 203 |
| Native | 72 |
| Hispanic/Latino | 1911 |
| Bachelor's or higher | 4920 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 19](/us/states/ar/districts/senate/19.md) — 100% (state senate)
- [AR House District 33](/us/states/ar/districts/house/33.md) — 53% (state house)
- [AR House District 34](/us/states/ar/districts/house/34.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
