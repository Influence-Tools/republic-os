---
type: Jurisdiction
title: "Westmoreland County, PA"
classification: county
fips: "42129"
state: "PA"
demographics:
  population: 352500
  population_under_18: 64150
  population_18_64: 202708
  population_65_plus: 85642
  median_household_income: 74109
  poverty_rate: 10.27
  homeownership_rate: 78.42
  unemployment_rate: 4.78
  median_home_value: 203500
  gini_index: 0.4537
  vacancy_rate: 8.19
  race_white: 323709
  race_black: 9148
  race_asian: 3406
  race_native: 295
  hispanic: 5692
  bachelors_plus: 117251
districts:
  - to: "us/states/pa/districts/14"
    rel: in-district
    area_weight: 0.8498
  - to: "us/states/pa/districts/12"
    rel: in-district
    area_weight: 0.149
  - to: "us/states/pa/districts/senate/39"
    rel: in-district
    area_weight: 0.5846
  - to: "us/states/pa/districts/senate/41"
    rel: in-district
    area_weight: 0.414
  - to: "us/states/pa/districts/house/59"
    rel: in-district
    area_weight: 0.4402
  - to: "us/states/pa/districts/house/55"
    rel: in-district
    area_weight: 0.2158
  - to: "us/states/pa/districts/house/58"
    rel: in-district
    area_weight: 0.1602
  - to: "us/states/pa/districts/house/57"
    rel: in-district
    area_weight: 0.0857
  - to: "us/states/pa/districts/house/56"
    rel: in-district
    area_weight: 0.0564
  - to: "us/states/pa/districts/house/60"
    rel: in-district
    area_weight: 0.0413
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Westmoreland County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 352500 |
| Under 18 | 64150 |
| 18–64 | 202708 |
| 65+ | 85642 |
| Median household income | 74109 |
| Poverty rate | 10.27 |
| Homeownership rate | 78.42 |
| Unemployment rate | 4.78 |
| Median home value | 203500 |
| Gini index | 0.4537 |
| Vacancy rate | 8.19 |
| White | 323709 |
| Black | 9148 |
| Asian | 3406 |
| Native | 295 |
| Hispanic/Latino | 5692 |
| Bachelor's or higher | 117251 |

## Districts

- [PA-14](/us/states/pa/districts/14.md) — 85% (congressional)
- [PA-12](/us/states/pa/districts/12.md) — 15% (congressional)
- [PA Senate District 39](/us/states/pa/districts/senate/39.md) — 58% (state senate)
- [PA Senate District 41](/us/states/pa/districts/senate/41.md) — 41% (state senate)
- [PA House District 59](/us/states/pa/districts/house/59.md) — 44% (state house)
- [PA House District 55](/us/states/pa/districts/house/55.md) — 22% (state house)
- [PA House District 58](/us/states/pa/districts/house/58.md) — 16% (state house)
- [PA House District 57](/us/states/pa/districts/house/57.md) — 9% (state house)
- [PA House District 56](/us/states/pa/districts/house/56.md) — 6% (state house)
- [PA House District 60](/us/states/pa/districts/house/60.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
