---
type: Jurisdiction
title: "Erie County, NY"
classification: county
fips: "36029"
state: "NY"
demographics:
  population: 950622
  population_under_18: 191431
  population_18_64: 575841
  population_65_plus: 183350
  median_household_income: 72839
  poverty_rate: 13.85
  homeownership_rate: 65.82
  unemployment_rate: 4.87
  median_home_value: 233800
  gini_index: 0.4637
  vacancy_rate: 7.15
  race_white: 699174
  race_black: 118588
  race_asian: 46784
  race_native: 3857
  hispanic: 60918
  bachelors_plus: 371632
districts:
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 0.6867
  - to: "us/states/ny/districts/26"
    rel: in-district
    area_weight: 0.1718
  - to: "us/states/ny/districts/senate/60"
    rel: in-district
    area_weight: 0.7042
  - to: "us/states/ny/districts/senate/61"
    rel: in-district
    area_weight: 0.0989
  - to: "us/states/ny/districts/senate/63"
    rel: in-district
    area_weight: 0.0559
  - to: "us/states/ny/districts/house/147"
    rel: in-district
    area_weight: 0.4979
  - to: "us/states/ny/districts/house/144"
    rel: in-district
    area_weight: 0.1088
  - to: "us/states/ny/districts/house/142"
    rel: in-district
    area_weight: 0.0448
  - to: "us/states/ny/districts/house/149"
    rel: in-district
    area_weight: 0.0444
  - to: "us/states/ny/districts/house/146"
    rel: in-district
    area_weight: 0.0438
  - to: "us/states/ny/districts/house/143"
    rel: in-district
    area_weight: 0.0334
  - to: "us/states/ny/districts/house/145"
    rel: in-district
    area_weight: 0.0273
  - to: "us/states/ny/districts/house/140"
    rel: in-district
    area_weight: 0.0225
  - to: "us/states/ny/districts/house/150"
    rel: in-district
    area_weight: 0.0209
  - to: "us/states/ny/districts/house/141"
    rel: in-district
    area_weight: 0.0139
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Erie County, NY

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 950622 |
| Under 18 | 191431 |
| 18–64 | 575841 |
| 65+ | 183350 |
| Median household income | 72839 |
| Poverty rate | 13.85 |
| Homeownership rate | 65.82 |
| Unemployment rate | 4.87 |
| Median home value | 233800 |
| Gini index | 0.4637 |
| Vacancy rate | 7.15 |
| White | 699174 |
| Black | 118588 |
| Asian | 46784 |
| Native | 3857 |
| Hispanic/Latino | 60918 |
| Bachelor's or higher | 371632 |

## Districts

- [NY-23](/us/states/ny/districts/23.md) — 69% (congressional)
- [NY-26](/us/states/ny/districts/26.md) — 17% (congressional)
- [NY Senate District 60](/us/states/ny/districts/senate/60.md) — 70% (state senate)
- [NY Senate District 61](/us/states/ny/districts/senate/61.md) — 10% (state senate)
- [NY Senate District 63](/us/states/ny/districts/senate/63.md) — 6% (state senate)
- [NY House District 147](/us/states/ny/districts/house/147.md) — 50% (state house)
- [NY House District 144](/us/states/ny/districts/house/144.md) — 11% (state house)
- [NY House District 142](/us/states/ny/districts/house/142.md) — 4% (state house)
- [NY House District 149](/us/states/ny/districts/house/149.md) — 4% (state house)
- [NY House District 146](/us/states/ny/districts/house/146.md) — 4% (state house)
- [NY House District 143](/us/states/ny/districts/house/143.md) — 3% (state house)
- [NY House District 145](/us/states/ny/districts/house/145.md) — 3% (state house)
- [NY House District 140](/us/states/ny/districts/house/140.md) — 2% (state house)
- [NY House District 150](/us/states/ny/districts/house/150.md) — 2% (state house)
- [NY House District 141](/us/states/ny/districts/house/141.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
