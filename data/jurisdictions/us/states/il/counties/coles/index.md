---
type: Jurisdiction
title: "Coles County, IL"
classification: county
fips: "17029"
state: "IL"
demographics:
  population: 46777
  population_under_18: 8549
  population_18_64: 29636
  population_65_plus: 8592
  median_household_income: 56478
  poverty_rate: 18.7
  homeownership_rate: 60.38
  unemployment_rate: 6.12
  median_home_value: 127400
  gini_index: 0.4519
  vacancy_rate: 8.19
  race_white: 41961
  race_black: 1670
  race_asian: 624
  race_native: 20
  hispanic: 1809
  bachelors_plus: 11520
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.5275
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.4725
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/101"
    rel: in-district
    area_weight: 0.7102
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.2897
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Coles County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46777 |
| Under 18 | 8549 |
| 18–64 | 29636 |
| 65+ | 8592 |
| Median household income | 56478 |
| Poverty rate | 18.7 |
| Homeownership rate | 60.38 |
| Unemployment rate | 6.12 |
| Median home value | 127400 |
| Gini index | 0.4519 |
| Vacancy rate | 8.19 |
| White | 41961 |
| Black | 1670 |
| Asian | 624 |
| Native | 20 |
| Hispanic/Latino | 1809 |
| Bachelor's or higher | 11520 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 53% (congressional)
- [IL-15](/us/states/il/districts/15.md) — 47% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 100% (state senate)
- [IL House District 101](/us/states/il/districts/house/101.md) — 71% (state house)
- [IL House District 102](/us/states/il/districts/house/102.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
