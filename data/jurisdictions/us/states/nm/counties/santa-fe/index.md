---
type: Jurisdiction
title: "Santa Fe County, NM"
classification: county
fips: "35049"
state: "NM"
demographics:
  population: 156105
  population_under_18: 25077
  population_18_64: 87243
  population_65_plus: 43785
  median_household_income: 79071
  poverty_rate: 11.97
  homeownership_rate: 71.51
  unemployment_rate: 5.26
  median_home_value: 446300
  gini_index: 0.4872
  vacancy_rate: 10.23
  race_white: 88445
  race_black: 1540
  race_asian: 2271
  race_native: 5097
  hispanic: 74740
  bachelors_plus: 84021
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.9333
  - to: "us/states/nm/districts/01"
    rel: in-district
    area_weight: 0.0667
  - to: "us/states/nm/districts/senate/39"
    rel: in-district
    area_weight: 0.3573
  - to: "us/states/nm/districts/senate/19"
    rel: in-district
    area_weight: 0.2597
  - to: "us/states/nm/districts/senate/25"
    rel: in-district
    area_weight: 0.218
  - to: "us/states/nm/districts/senate/6"
    rel: in-district
    area_weight: 0.1534
  - to: "us/states/nm/districts/senate/24"
    rel: in-district
    area_weight: 0.0078
  - to: "us/states/nm/districts/house/50"
    rel: in-district
    area_weight: 0.5389
  - to: "us/states/nm/districts/house/46"
    rel: in-district
    area_weight: 0.2504
  - to: "us/states/nm/districts/house/47"
    rel: in-district
    area_weight: 0.1256
  - to: "us/states/nm/districts/house/43"
    rel: in-district
    area_weight: 0.0736
  - to: "us/states/nm/districts/house/45"
    rel: in-district
    area_weight: 0.0066
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Santa Fe County, NM

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 156105 |
| Under 18 | 25077 |
| 18–64 | 87243 |
| 65+ | 43785 |
| Median household income | 79071 |
| Poverty rate | 11.97 |
| Homeownership rate | 71.51 |
| Unemployment rate | 5.26 |
| Median home value | 446300 |
| Gini index | 0.4872 |
| Vacancy rate | 10.23 |
| White | 88445 |
| Black | 1540 |
| Asian | 2271 |
| Native | 5097 |
| Hispanic/Latino | 74740 |
| Bachelor's or higher | 84021 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 93% (congressional)
- [NM-01](/us/states/nm/districts/01.md) — 7% (congressional)
- [NM Senate District 39](/us/states/nm/districts/senate/39.md) — 36% (state senate)
- [NM Senate District 19](/us/states/nm/districts/senate/19.md) — 26% (state senate)
- [NM Senate District 25](/us/states/nm/districts/senate/25.md) — 22% (state senate)
- [NM Senate District 6](/us/states/nm/districts/senate/6.md) — 15% (state senate)
- [NM Senate District 24](/us/states/nm/districts/senate/24.md) — 1% (state senate)
- [NM House District 50](/us/states/nm/districts/house/50.md) — 54% (state house)
- [NM House District 46](/us/states/nm/districts/house/46.md) — 25% (state house)
- [NM House District 47](/us/states/nm/districts/house/47.md) — 13% (state house)
- [NM House District 43](/us/states/nm/districts/house/43.md) — 7% (state house)
- [NM House District 45](/us/states/nm/districts/house/45.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
