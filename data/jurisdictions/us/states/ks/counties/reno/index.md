---
type: Jurisdiction
title: "Reno County, KS"
classification: county
fips: "20155"
state: "KS"
demographics:
  population: 61553
  population_under_18: 13518
  population_18_64: 35376
  population_65_plus: 12659
  median_household_income: 60645
  poverty_rate: 12.52
  homeownership_rate: 69.19
  unemployment_rate: 3.89
  median_home_value: 132500
  gini_index: 0.4267
  vacancy_rate: 9.49
  race_white: 52333
  race_black: 1667
  race_asian: 342
  race_native: 485
  hispanic: 6388
  bachelors_plus: 11578
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ks/districts/senate/34"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/114"
    rel: in-district
    area_weight: 0.7417
  - to: "us/states/ks/districts/house/101"
    rel: in-district
    area_weight: 0.1738
  - to: "us/states/ks/districts/house/104"
    rel: in-district
    area_weight: 0.071
  - to: "us/states/ks/districts/house/102"
    rel: in-district
    area_weight: 0.0134
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Reno County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61553 |
| Under 18 | 13518 |
| 18–64 | 35376 |
| 65+ | 12659 |
| Median household income | 60645 |
| Poverty rate | 12.52 |
| Homeownership rate | 69.19 |
| Unemployment rate | 3.89 |
| Median home value | 132500 |
| Gini index | 0.4267 |
| Vacancy rate | 9.49 |
| White | 52333 |
| Black | 1667 |
| Asian | 342 |
| Native | 485 |
| Hispanic/Latino | 6388 |
| Bachelor's or higher | 11578 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 34](/us/states/ks/districts/senate/34.md) — 100% (state senate)
- [KS House District 114](/us/states/ks/districts/house/114.md) — 74% (state house)
- [KS House District 101](/us/states/ks/districts/house/101.md) — 17% (state house)
- [KS House District 104](/us/states/ks/districts/house/104.md) — 7% (state house)
- [KS House District 102](/us/states/ks/districts/house/102.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
