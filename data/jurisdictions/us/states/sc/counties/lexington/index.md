---
type: Jurisdiction
title: "Lexington County, SC"
classification: county
fips: "45063"
state: "SC"
demographics:
  population: 304887
  population_under_18: 70033
  population_18_64: 182765
  population_65_plus: 52089
  median_household_income: 77408
  poverty_rate: 11.11
  homeownership_rate: 77.4
  unemployment_rate: 4.46
  median_home_value: 234500
  gini_index: 0.4289
  vacancy_rate: 8.24
  race_white: 219424
  race_black: 46578
  race_asian: 6738
  race_native: 792
  hispanic: 24118
  bachelors_plus: 99915
districts:
  - to: "us/states/sc/districts/02"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/sc/districts/senate/23"
    rel: in-district
    area_weight: 0.463
  - to: "us/states/sc/districts/senate/25"
    rel: in-district
    area_weight: 0.1657
  - to: "us/states/sc/districts/senate/26"
    rel: in-district
    area_weight: 0.1608
  - to: "us/states/sc/districts/senate/18"
    rel: in-district
    area_weight: 0.1113
  - to: "us/states/sc/districts/senate/10"
    rel: in-district
    area_weight: 0.0991
  - to: "us/states/sc/districts/house/39"
    rel: in-district
    area_weight: 0.2189
  - to: "us/states/sc/districts/house/96"
    rel: in-district
    area_weight: 0.2141
  - to: "us/states/sc/districts/house/86"
    rel: in-district
    area_weight: 0.1022
  - to: "us/states/sc/districts/house/87"
    rel: in-district
    area_weight: 0.0942
  - to: "us/states/sc/districts/house/93"
    rel: in-district
    area_weight: 0.0898
  - to: "us/states/sc/districts/house/85"
    rel: in-district
    area_weight: 0.0837
  - to: "us/states/sc/districts/house/88"
    rel: in-district
    area_weight: 0.0831
  - to: "us/states/sc/districts/house/69"
    rel: in-district
    area_weight: 0.05
  - to: "us/states/sc/districts/house/89"
    rel: in-district
    area_weight: 0.0425
  - to: "us/states/sc/districts/house/40"
    rel: in-district
    area_weight: 0.0152
  - to: "us/states/sc/districts/house/71"
    rel: in-district
    area_weight: 0.0061
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Lexington County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 304887 |
| Under 18 | 70033 |
| 18–64 | 182765 |
| 65+ | 52089 |
| Median household income | 77408 |
| Poverty rate | 11.11 |
| Homeownership rate | 77.4 |
| Unemployment rate | 4.46 |
| Median home value | 234500 |
| Gini index | 0.4289 |
| Vacancy rate | 8.24 |
| White | 219424 |
| Black | 46578 |
| Asian | 6738 |
| Native | 792 |
| Hispanic/Latino | 24118 |
| Bachelor's or higher | 99915 |

## Districts

- [SC-02](/us/states/sc/districts/02.md) — 100% (congressional)
- [SC Senate District 23](/us/states/sc/districts/senate/23.md) — 46% (state senate)
- [SC Senate District 25](/us/states/sc/districts/senate/25.md) — 17% (state senate)
- [SC Senate District 26](/us/states/sc/districts/senate/26.md) — 16% (state senate)
- [SC Senate District 18](/us/states/sc/districts/senate/18.md) — 11% (state senate)
- [SC Senate District 10](/us/states/sc/districts/senate/10.md) — 10% (state senate)
- [SC House District 39](/us/states/sc/districts/house/39.md) — 22% (state house)
- [SC House District 96](/us/states/sc/districts/house/96.md) — 21% (state house)
- [SC House District 86](/us/states/sc/districts/house/86.md) — 10% (state house)
- [SC House District 87](/us/states/sc/districts/house/87.md) — 9% (state house)
- [SC House District 93](/us/states/sc/districts/house/93.md) — 9% (state house)
- [SC House District 85](/us/states/sc/districts/house/85.md) — 8% (state house)
- [SC House District 88](/us/states/sc/districts/house/88.md) — 8% (state house)
- [SC House District 69](/us/states/sc/districts/house/69.md) — 5% (state house)
- [SC House District 89](/us/states/sc/districts/house/89.md) — 4% (state house)
- [SC House District 40](/us/states/sc/districts/house/40.md) — 2% (state house)
- [SC House District 71](/us/states/sc/districts/house/71.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
