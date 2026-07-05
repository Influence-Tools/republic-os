---
type: Jurisdiction
title: "Venango County, PA"
classification: county
fips: "42121"
state: "PA"
demographics:
  population: 49801
  population_under_18: 9469
  population_18_64: 27986
  population_65_plus: 12346
  median_household_income: 61522
  poverty_rate: 13.15
  homeownership_rate: 75.29
  unemployment_rate: 5.6
  median_home_value: 119800
  gini_index: 0.4145
  vacancy_rate: 18.47
  race_white: 46630
  race_black: 628
  race_asian: 156
  race_native: 45
  hispanic: 639
  bachelors_plus: 9588
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 0.6865
  - to: "us/states/pa/districts/16"
    rel: in-district
    area_weight: 0.3135
  - to: "us/states/pa/districts/senate/21"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/house/64"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Venango County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49801 |
| Under 18 | 9469 |
| 18–64 | 27986 |
| 65+ | 12346 |
| Median household income | 61522 |
| Poverty rate | 13.15 |
| Homeownership rate | 75.29 |
| Unemployment rate | 5.6 |
| Median home value | 119800 |
| Gini index | 0.4145 |
| Vacancy rate | 18.47 |
| White | 46630 |
| Black | 628 |
| Asian | 156 |
| Native | 45 |
| Hispanic/Latino | 639 |
| Bachelor's or higher | 9588 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 69% (congressional)
- [PA-16](/us/states/pa/districts/16.md) — 31% (congressional)
- [PA Senate District 21](/us/states/pa/districts/senate/21.md) — 100% (state senate)
- [PA House District 64](/us/states/pa/districts/house/64.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
