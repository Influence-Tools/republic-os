---
type: Jurisdiction
title: "Mountrail County, ND"
classification: county
fips: "38061"
state: "ND"
demographics:
  population: 9507
  population_under_18: 2760
  population_18_64: 5462
  population_65_plus: 1285
  median_household_income: 80717
  poverty_rate: 14.52
  homeownership_rate: 61.55
  unemployment_rate: 1.08
  median_home_value: 232700
  gini_index: 0.4805
  vacancy_rate: 23.49
  race_white: 5485
  race_black: 175
  race_asian: 54
  race_native: 2750
  hispanic: 819
  bachelors_plus: 1861
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/4"
    rel: in-district
    area_weight: 0.7755
  - to: "us/states/nd/districts/senate/2"
    rel: in-district
    area_weight: 0.2245
  - to: "us/states/nd/districts/house/4b"
    rel: in-district
    area_weight: 0.5613
  - to: "us/states/nd/districts/house/2"
    rel: in-district
    area_weight: 0.2245
  - to: "us/states/nd/districts/house/4a"
    rel: in-district
    area_weight: 0.2141
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Mountrail County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9507 |
| Under 18 | 2760 |
| 18–64 | 5462 |
| 65+ | 1285 |
| Median household income | 80717 |
| Poverty rate | 14.52 |
| Homeownership rate | 61.55 |
| Unemployment rate | 1.08 |
| Median home value | 232700 |
| Gini index | 0.4805 |
| Vacancy rate | 23.49 |
| White | 5485 |
| Black | 175 |
| Asian | 54 |
| Native | 2750 |
| Hispanic/Latino | 819 |
| Bachelor's or higher | 1861 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 4](/us/states/nd/districts/senate/4.md) — 78% (state senate)
- [ND Senate District 2](/us/states/nd/districts/senate/2.md) — 22% (state senate)
- [ND House District 4B](/us/states/nd/districts/house/4b.md) — 56% (state house)
- [ND House District 2](/us/states/nd/districts/house/2.md) — 22% (state house)
- [ND House District 4A](/us/states/nd/districts/house/4a.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
