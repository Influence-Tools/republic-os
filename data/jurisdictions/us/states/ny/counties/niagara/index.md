---
type: Jurisdiction
title: "Niagara County, NY"
classification: county
fips: "36063"
state: "NY"
demographics:
  population: 210721
  population_under_18: 41850
  population_18_64: 125183
  population_65_plus: 43688
  median_household_income: 69633
  poverty_rate: 13.53
  homeownership_rate: 71.16
  unemployment_rate: 5.92
  median_home_value: 189800
  gini_index: 0.4437
  vacancy_rate: 8.52
  race_white: 174788
  race_black: 13944
  race_asian: 2483
  race_native: 1194
  hispanic: 8459
  bachelors_plus: 60405
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.3643
  - to: "us/states/ny/districts/26"
    rel: in-district
    area_weight: 0.0562
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 0.0454
  - to: "us/states/ny/districts/senate/62"
    rel: in-district
    area_weight: 0.4656
  - to: "us/states/ny/districts/house/144"
    rel: in-district
    area_weight: 0.2993
  - to: "us/states/ny/districts/house/145"
    rel: in-district
    area_weight: 0.1593
  - to: "us/states/ny/districts/house/140"
    rel: in-district
    area_weight: 0.0064
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Niagara County, NY

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 210721 |
| Under 18 | 41850 |
| 18–64 | 125183 |
| 65+ | 43688 |
| Median household income | 69633 |
| Poverty rate | 13.53 |
| Homeownership rate | 71.16 |
| Unemployment rate | 5.92 |
| Median home value | 189800 |
| Gini index | 0.4437 |
| Vacancy rate | 8.52 |
| White | 174788 |
| Black | 13944 |
| Asian | 2483 |
| Native | 1194 |
| Hispanic/Latino | 8459 |
| Bachelor's or higher | 60405 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 36% (congressional)
- [NY-26](/us/states/ny/districts/26.md) — 6% (congressional)
- [NY-23](/us/states/ny/districts/23.md) — 5% (congressional)
- [NY Senate District 62](/us/states/ny/districts/senate/62.md) — 47% (state senate)
- [NY House District 144](/us/states/ny/districts/house/144.md) — 30% (state house)
- [NY House District 145](/us/states/ny/districts/house/145.md) — 16% (state house)
- [NY House District 140](/us/states/ny/districts/house/140.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
