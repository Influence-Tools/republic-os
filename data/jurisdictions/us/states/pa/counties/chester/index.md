---
type: Jurisdiction
title: "Chester County, PA"
classification: county
fips: "42029"
state: "PA"
demographics:
  population: 547840
  population_under_18: 120444
  population_18_64: 330280
  population_65_plus: 97116
  median_household_income: 127208
  poverty_rate: 5.98
  homeownership_rate: 75.05
  unemployment_rate: 3.77
  median_home_value: 485600
  gini_index: 0.4469
  vacancy_rate: 3.63
  race_white: 422108
  race_black: 28542
  race_asian: 37240
  race_native: 604
  hispanic: 45958
  bachelors_plus: 306773
districts:
  - to: "us/states/pa/districts/06"
    rel: in-district
    area_weight: 0.9956
  - to: "us/states/pa/districts/senate/19"
    rel: in-district
    area_weight: 0.4322
  - to: "us/states/pa/districts/senate/44"
    rel: in-district
    area_weight: 0.4004
  - to: "us/states/pa/districts/senate/9"
    rel: in-district
    area_weight: 0.1671
  - to: "us/states/pa/districts/house/13"
    rel: in-district
    area_weight: 0.25
  - to: "us/states/pa/districts/house/158"
    rel: in-district
    area_weight: 0.1587
  - to: "us/states/pa/districts/house/26"
    rel: in-district
    area_weight: 0.1438
  - to: "us/states/pa/districts/house/74"
    rel: in-district
    area_weight: 0.1095
  - to: "us/states/pa/districts/house/167"
    rel: in-district
    area_weight: 0.0947
  - to: "us/states/pa/districts/house/155"
    rel: in-district
    area_weight: 0.0835
  - to: "us/states/pa/districts/house/157"
    rel: in-district
    area_weight: 0.0729
  - to: "us/states/pa/districts/house/156"
    rel: in-district
    area_weight: 0.0482
  - to: "us/states/pa/districts/house/160"
    rel: in-district
    area_weight: 0.0383
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Chester County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 547840 |
| Under 18 | 120444 |
| 18–64 | 330280 |
| 65+ | 97116 |
| Median household income | 127208 |
| Poverty rate | 5.98 |
| Homeownership rate | 75.05 |
| Unemployment rate | 3.77 |
| Median home value | 485600 |
| Gini index | 0.4469 |
| Vacancy rate | 3.63 |
| White | 422108 |
| Black | 28542 |
| Asian | 37240 |
| Native | 604 |
| Hispanic/Latino | 45958 |
| Bachelor's or higher | 306773 |

## Districts

- [PA-06](/us/states/pa/districts/06.md) — 100% (congressional)
- [PA Senate District 19](/us/states/pa/districts/senate/19.md) — 43% (state senate)
- [PA Senate District 44](/us/states/pa/districts/senate/44.md) — 40% (state senate)
- [PA Senate District 9](/us/states/pa/districts/senate/9.md) — 17% (state senate)
- [PA House District 13](/us/states/pa/districts/house/13.md) — 25% (state house)
- [PA House District 158](/us/states/pa/districts/house/158.md) — 16% (state house)
- [PA House District 26](/us/states/pa/districts/house/26.md) — 14% (state house)
- [PA House District 74](/us/states/pa/districts/house/74.md) — 11% (state house)
- [PA House District 167](/us/states/pa/districts/house/167.md) — 9% (state house)
- [PA House District 155](/us/states/pa/districts/house/155.md) — 8% (state house)
- [PA House District 157](/us/states/pa/districts/house/157.md) — 7% (state house)
- [PA House District 156](/us/states/pa/districts/house/156.md) — 5% (state house)
- [PA House District 160](/us/states/pa/districts/house/160.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
